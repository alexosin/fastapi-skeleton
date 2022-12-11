# {{ cookiecutter.project_name }}

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Installation and Usage

### Installation

Install Python {{ cookiecutter.python_version }} & setup virtual environment

```bash
pyenv install {{ cookiecutter.patch_python_version }}
pyenv virtualenv {{ cookiecutter.patch_python_version }} {{ cookiecutter.project_slug }}
pyenv activate {{ cookiecutter.project_slug }}
```

Install Python requirements:

```bash
pip install poetry
poetry install
```

### Usage

Create `.env` file:

```bash
cp .env.example .env
```

Run the server:

```bash
python -m uvicorn {{ cookiecutter.project_snake_name }}.main:app --reload
```

#### Usage with docker

All commands are executed from the docker directory:

```bash
cd docker
```

Init docker:

```bash
make init
```

Run services:

```bash
docker compose up
```
