.PHONY: setup dev test lint install

# Install all dependencies and setup the project
setup:
	uv sync
	uv run pre-commit install

# Setup local development environment with editable CLI installation
dev:
	uv sync
	uv run pre-commit install
	uv tool install --editable . --force

# Run all unit tests using pytest
test:
	uv run pytest

# Fix linting and format code using ruff
lint:
	uv run ruff check . --fix
	uv run ruff format .

# Install the SOLA CLI globally on the local system
install:
	uv tool install . --force
