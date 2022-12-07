import logging

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi_utils.tasks import repeat_every

from {{ cookiecutter.project_snake_name }}.core.config import settings
from {{ cookiecutter.project_snake_name }}.core.containers import Container
from {{ cookiecutter.project_snake_name }}.services import MainService


logger = logging.getLogger(__name__)


async def set_up_periodic_tasks():
    if settings.ENABLE_PERIODIC_TASKS:
        await spam_about_periodic_logic()


@inject
async def _inject_get_project_info(main_service: MainService = Depends(Provide[Container.main_service])):
    project_info = await main_service.get_project_info()
    logger.info(project_info)


@repeat_every(seconds=60, wait_first=True)
async def spam_about_periodic_logic() -> None:
    logger.warning("Setup periodic task or delete logic for that.")
    await _inject_get_project_info()
