from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import Environment, settings

# Uncomment when LangFuse is configured (run setup-langfuse skill first)
# from app.core.observability import init_observability


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Startup
    # init_observability()  # ← uncomment when LangFuse is configured
    yield
    # Shutdown


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    lifespan=lifespan,
    # Disable docs in production
    docs_url="/docs" if settings.app_env != Environment.PRODUCTION else None,
    redoc_url="/redoc" if settings.app_env != Environment.PRODUCTION else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    """Health check endpoint — used by deploy workflows."""
    return {"status": "ok"}


# Register routers here
# from app.api.routes.v1 import users
# app.include_router(users.router, prefix="/api/v1")
