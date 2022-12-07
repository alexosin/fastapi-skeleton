from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from {{ cookiecutter.project_snake_name }}.core.containers import Container
from {{ cookiecutter.project_snake_name }}.services import MainService


router = APIRouter()


@router.get("/")
async def index():
    return {"message": "{{ cookiecutter.project_name }} welcome page!"}


@router.get("/project-info/")
@inject
async def project_info(
    main_service: MainService = Depends(Provide[Container.main_service]),
):
    return await main_service.get_project_info()
