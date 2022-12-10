# Fastapi Backend Skeleton

[Fastapi](https://fastapi.tiangolo.com/) project template based on [cookiecutter](https://cookiecutter.readthedocs.io/).
## Features

- [Dependency Injector](https://python-dependency-injector.ets-labs.org/) - implement the support of DeclarativeContainer with:
    - config and container providers
    - wiring routes and periodic_tasks modules
- Support `docker` and `docker compose` for local and live environments.
- `pyproject.toml` support.
- `Poetry` tool for packages management.
- Built-in linters:
    - `black`
    - `isort`
    - `pylama`
    - `safety`
- Example of [repeated tasks](https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/) implementation in combination with `dependency-injector`.
- startup and shutdown events.

*WIP*:
- `pre-commit` config.
- Migration to `ruff` linter.

## How to use it

Go to the directory where you want to create your project and run:

```bash
cookiecutter https://github.com/alexosin/fastapi-skeleton.git
```

### Input variables

The generator (cookiecutter) will ask you for some data.

The input variables have default values or can be auto generated:

- `project_name`: the name of ther project
- `project_slug`: generated from `project_name`, using for main folder, docker images and containers
- `project_snake_name`: generated from `project_name`, using for naming of src directory
- `env_prefix`: the prefix for env variables
- `python_version`: python version with major and minor version numbers (example *3.10*)
- `patch_python_version`: python version with patch version number (example *3.10.2*), using for docker images
