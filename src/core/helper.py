import os
import stat

import docker
from docker import DockerClient
from docker.models.containers import Container
from docker.models.images import Image
from git import Repo, Remote

from .logging import LogType, log

docker_client: DockerClient = docker.from_env()
repositories: dict[str, Remote] = {}
containers: dict[str, Container] = {}


def get_repo_secrets(prefix: str) -> dict[str, str]:
    return {key[len(prefix) :]: value for key, value in os.environ.items() if key.startswith(prefix)}


def remove_readonly_permission(path, func, _):
    """Clear the readonly bit and reattempt the removal"""
    log(LogType.WARNING, f"Adjusting permissions to include S_IWRITE for {path}")

    os.chmod(path, stat.S_IWRITE)
    func(path)


def update_repository(repository_url: str, repository_name: str):
    if repository_name in repositories:
        log(LogType.INFO, f"Updating repository {repository_name} from {repository_url}")
        repositories[repository_name].pull()

    else:
        log(LogType.INFO, f"Cloning repository {repository_name} from {repository_url}")
        path: str = f"./repositories/{repository_name}"
        repository: Repo = Repo.clone_from(url=repository_url, to_path=path)
        repositories[repository_name] = repository.remote()


def deploy_repository(repository_name: str, repository_url: str):
    # Updating repository
    update_repository(repository_url, repository_name)

    # Create image from repo
    log(LogType.INFO, f"Building new image for repository {repository_name}")
    docker_image: Image = docker_client.images.build(
        path="./repositories/" + repository_name, tag=repository_name, rm=True
    )[0]

    # Removing currently existing container for repository
    if repository_name in containers:
        container: Container = containers.pop(repository_name)
        log(
            LogType.WARNING,
            f"Removing container {container.name} with image tags {container.image.tags}...",
        )
        container.stop()
        container.remove()

    # Start a new container with a new image
    log(LogType.INFO, f"Starting new container with new image {docker_image.tags}")
    container: Container = docker_client.containers.run(
        docker_image,
        name=repository_name,
        detach=True,
        network="host",
        environment=get_repo_secrets(repository_name),
    )

    containers[repository_name] = container
