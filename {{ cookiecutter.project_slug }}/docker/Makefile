.ONESHELL:

init-{{ cookiecutter.project_slug }}:
	@echo "Initializing {{ cookiecutter.project_slug }}..."
	@cp ../.env.example ../.env

init: init-{{ cookiecutter.project_slug }}
	@echo "Initializing docker..."
	@cp .env.example .env
