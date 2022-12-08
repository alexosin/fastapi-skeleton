from dependency_injector import containers, providers

from {{ cookiecutter.project_snake_name }}.core.config import settings
from {{ cookiecutter.project_snake_name }}.services import MainService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "{{ cookiecutter.project_snake_name }}.api.routes",
            "{{ cookiecutter.project_snake_name }}.periodic_tasks",
        ]
    )

    config = providers.Configuration(pydantic_settings=[settings])

    main_service = providers.Factory(MainService)
