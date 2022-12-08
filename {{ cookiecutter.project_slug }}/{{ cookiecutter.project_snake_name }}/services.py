from {{ cookiecutter.project_snake_name }}.core.config import settings


class MainService:
    async def get_project_info(self) -> dict:
        return {
            "project_name": settings.PROJECT_NAME,
            "mode": "debug" if settings.DEBUG else "live",
            "sentry_enabled": "yes" if settings.SENTRY_ON else "no",
        }
