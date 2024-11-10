import uvicorn
from fastapi import FastAPI, Request

from src.api import router as api_router
from src.core import LogType, log

app: FastAPI = FastAPI()
app.include_router(api_router)


@app.middleware("http")
async def middleware(request: Request, call_next):
    log(LogType.INFO, f"{request.method} {request.url.path}")

    return await call_next(request)


if __name__ == "__main__":
    print("\033[?25l", end="")

    try:
        log(LogType.INFO, "Starting uvicorn app")

        uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)

    except Exception as exception:
        log(LogType.ERROR, str(exception))
