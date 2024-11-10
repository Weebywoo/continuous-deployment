from fastapi import APIRouter

from .deployment import router as deployment_router

router: APIRouter = APIRouter(prefix="/api")
router.include_router(deployment_router)
