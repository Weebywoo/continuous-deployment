# CICD
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) ![GitHub License](https://img.shields.io/github/license/Weebywoo/CICD)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Weebywoo&repo=CICD)](https://github.com/anuraghazra/github-readme-stats)

### Logging

- [ ] Add "elapsed since started" log for ongoing requests
- [ ] Add advanced progress logging
- [x] 'WARNING' log type should be yellow
- [x] 'IN PROGRESS' type should be magenta
- [x] 'DONE' log type should be green
- [x] Rename 'DONE' to 'TASK DONE'
- [x] Add color to logging
- [x] Increase logging code coverage

### Docker

``/var/run/docker.sock:/var/run/docker.sock``

- [x] Add Dockerfile to project
- [x] Test inside of Docker image
- [x] Use host docker instance to start sibling containers
- [x] Replace existing container
- [x] Stop and remove all containers on shutdown
- [x] Fix docker-py starting multiple dockers
- [ ] Add the possibility to deploy many different repositories

### Network

- [x] Close ngrok session after quitting
- [x] Remove ngrok dependency

### GitHub

- [ ] Only redeploy on master or main push or merge

### Big changes

- [ ] Upon push application should start new container with new instance of itself with new image and replace itself,
  shutting down the old container