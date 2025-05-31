from fastapi import FastAPI
from apps.auth.api import router as auth_router
from src.containers import AppContainer

app = FastAPI(title="DI Slam Dunks")

# Configure dependency injection
container = AppContainer()
container.wire(modules=[__name__])

# Include routers
app.include_router(auth_router, prefix="/auth") 