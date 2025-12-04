from fastapi import FastAPI
from src.apps.auth.api import router as auth_router
from src.containers import AppContainer

app = FastAPI(title="DI Slam Dunks")


container = AppContainer()
container.wire(modules=[__name__])

app.include_router(auth_router, prefix="/auth") 