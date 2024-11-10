from fastapi import APIRouter, status, HTTPException

from src.core.helper import deploy_repository
from src.core.logging import LogType, log

router: APIRouter = APIRouter(prefix="/deployment", tags=["deployment"])


@router.post(path="", status_code=status.HTTP_201_CREATED)
async def deploy_repository_endpoint(body: dict):
    try:
        repository_name: str = body["repository"]["name"]
        repository_url: str = body["repository"]["html_url"] + ".git"

        deploy_repository(repository_name, repository_url)

    except Exception as exception:
        log(LogType.ERROR, str(exception))

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exception))
