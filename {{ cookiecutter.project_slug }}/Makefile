safety-check:
	safety check

isort-check:
	isort --check --skip .env --resolve-all-configs .

black-check:
	black --check .

bandit:
	bandit -c pyproject.toml -r .

pylama:
	pylama

linters-check: isort-check black-check bandit pylama safety-check

pytest:
	pytest --cov=./{{ cookiecutter.project_snake_name }} --cov-report xml
