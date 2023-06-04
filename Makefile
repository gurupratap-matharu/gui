
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
	pip install -r requirements.txt

isort:
	@echo "isort..."
	@python -m isort . --profile black

format:
	@echo "black..."
	@python -m black . 

lint: isort format
	@echo "flake8..."
	@python -m flake8 .

ci: lint 

run:
	python calculator.py

reload:
	@echo "reloading..."
	@echo "All done! 💅💫💖"
