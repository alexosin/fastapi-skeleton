FROM python:{{ cookiecutter.patch_python_version }}-slim as base

ARG DOCKER_USER_ID=1000
ARG DOCKER_GROUP_ID=1000

ENV PYTHONUNBUFFERED 1

RUN groupadd -g ${DOCKER_GROUP_ID} user \
    && useradd --shell /bin/bash -u $DOCKER_USER_ID -g $DOCKER_GROUP_ID -o -c "" -m user

RUN apt-get update \
    && apt-get install --no-install-recommends -y build-essential  \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

RUN pip install --no-cache -U pip setuptools poetry \
    && rm -rf /root/.cache/pip

COPY --chown=user:user ./pyproject.toml \
    ./poetry.lock /opt/{{ cookiecutter.project_slug }}/

ENV PYTHONPATH /opt/{{ cookiecutter.project_slug }}

WORKDIR /opt/{{ cookiecutter.project_slug }}

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev \
    && rm -rf /root/.cache/pypoetry

FROM base as local

USER root

RUN poetry install --no-interaction --no-ansi \
    && rm -rf /root/.cache/pypoetry

USER user

CMD ["uvicorn", "--host", "0.0.0.0", "{{ cookiecutter.project_snake_name }}.main:app", "--reload"]


FROM base as live

COPY --chown=user:user ./{{ cookiecutter.project_slug }} /opt/{{ cookiecutter.project_slug }}/

CMD [ \
    "gunicorn", \
    "{{ cookiecutter.project_snake_name }}.main:app", \
    "--bind", "0.0.0.0", \
    "--worker-class", "uvicorn.workers.UvicornWorker", \
    "--access-logfile", "-", "--error-logfile", "-" \
    ]
