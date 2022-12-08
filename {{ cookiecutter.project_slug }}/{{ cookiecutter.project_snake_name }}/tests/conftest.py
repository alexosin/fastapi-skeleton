import pytest

from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient

from {{ cookiecutter.project_snake_name }}.core.config import settings
from {{ cookiecutter.project_snake_name }}.main import get_application


@pytest.fixture()
async def app() -> FastAPI:
    settings.DEBUG = True
    settings.SENTRY_ON = False
    # Disable periodic tasks for tests
    settings.ENABLE_PERIODIC_TASKS = False
    app = get_application()
    return app


@pytest.fixture(autouse=True)
async def initialized_app(app: FastAPI) -> FastAPI:
    async with LifespanManager(app):
        app.container.init_resources()
        yield app


@pytest.fixture()
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
    ) as client:
        yield client
