from fastapi import status
from httpx import AsyncClient

from {{ cookiecutter.project_snake_name }}.api.routes import router
from {{ cookiecutter.project_snake_name }}.core.config import settings


async def test_read_home_success(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == status.HTTP_200_OK


async def test_project_info(client: AsyncClient):
    url = router.url_path_for("project_info")
    response = await client.get(url)
    assert response == {
        "project_name": settings.PROJECT_NAME,
        "mode": "debug",
        "sentry_enabled": "no",
    }
