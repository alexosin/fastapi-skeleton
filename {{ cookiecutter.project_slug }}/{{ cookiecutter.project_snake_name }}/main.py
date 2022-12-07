import sentry_sdk

from fastapi import FastAPI

from {{ cookiecutter.project_snake_name }}.api import routes
from {{ cookiecutter.project_snake_name }}.core.config import settings
from {{ cookiecutter.project_snake_name }}.core.containers import Container
from {{ cookiecutter.project_snake_name }}.core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    container = Container()

    application = FastAPI(
        title=settings.PROJECT_NAME,
        root_path=settings.API_ROOT_PATH,
        debug=settings.DEBUG,
    )
    application.container = container
    application.add_event_handler("startup", create_start_app_handler())
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(routes.router)

    if settings.SENTRY_ON:
        sentry_sdk.init(dsn=settings.SENTRY_DSN, environment=settings.SENTRY_ENVIRONMENT)

    return application


app = get_application()
