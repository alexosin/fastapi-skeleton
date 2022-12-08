import logging
import sys

from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "{{ cookiecutter.project_name }}"
    DEBUG: bool = False
    API_ROOT_PATH: str = ""

    SENTRY_ON: bool = False
    SENTRY_DSN: AnyUrl = None
    SENTRY_ENVIRONMENT: str = ""

    ENABLE_PERIODIC_TASKS: bool = True

    class Config:
        env_prefix = "{{ cookiecutter.env_prefix }}"
        env_file = ".env"
        case_sensitive = True


settings = Settings()

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG if settings.DEBUG else logging.ERROR,
)
