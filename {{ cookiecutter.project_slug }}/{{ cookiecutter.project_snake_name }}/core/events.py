import logging

from typing import Callable

from dependency_injector import providers
from fastapi import FastAPI

from {{ cookiecutter.project_snake_name }} import periodic_tasks


logger = logging.getLogger(__name__)


async def shutdown_resources(container):
    logger.debug("Shutdown resources started.")
    for provider in container.traverse(types=[providers.Resource]):
        if provider.initialized:
            await container.shutdown_resources()
            break
    logger.debug("Shutdown resources finished.")


def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        await periodic_tasks.set_up_periodic_tasks()

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await shutdown_resources(app.container)

    return stop_app
