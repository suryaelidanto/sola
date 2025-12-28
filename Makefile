.PHONY: setup dev test lint install

setup:
	uv sync

dev:
	uv sync
	uv tool install --editable . --force

test:
	uv run pytest

lint:
	uv run ruff check . --fix
	uv run ruff format .

install:
	uv tool install . --force
