
APP_LIST ?= main src 
.PHONY: dist build 

help:
	@echo "Available commands"
	@echo " - ci               : lints, migrations, tests, coverage"
	@echo " - install          : installs production requirements"
	@echo " - install-dev      : installs development requirements"
	@echo " - isort            : sorts all imports of the project"
	@echo " - lint             : lints the codebase"
	@echo " - run              : runs the development server"

clean:
	rm -rf __pycache__ .pytest_cache

install:
	poetry install

update:
	poetry update

isort:
	@echo "isort..."
	@poetry run isort . --profile black

format:
	@echo "black..."
	@poetry run black . 

lint: isort format
	@echo "flake8..."
	@poetry run flake8 .

ci: lint 

run:
	python hello.py

reload:
	@echo "reloading..."
	@echo "All done! 💅💫💖"
