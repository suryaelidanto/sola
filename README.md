# SOLA: Standardized Orchestration & Logic Architecture

![CI Status](https://github.com/suryaelidanto/sola/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

SOLA is an opinionated CLI tool designed for AI Engineers to scaffold production-ready microservices. It enforces clean architecture, standardized infrastructure, and leverages LLMs for autonomous business logic generation.

## Core Philosophy
1.  **Architecture over Boilerplate:** Every project starts with a modular, enterprise-ready structure.
2.  **Infrastructure as a Standard:** Automated generation of `Makefile`, `Dockerfile`, and CI/CD configurations.
3.  **AI-Native Engineering:** An integrated "AI Architect" to forge specialized business logic directly into the services layer.

---

## Technical Features
-   **Structured Scaffolding:** Modular layout (`app/`, `tests/`) with built-in Python packaging best practices.
-   **Dependency Orchestration:** Powered by `uv` for ultra-fast environment management.
-   **Templating Engine:** Uses `Jinja2` for consistent file generation.
-   **CLI UX:** Rich terminal output and interactive prompts via `Typer` and `Rich`.

---

## Prerequisites
- **Python**: 3.10 or higher
- **UV**: Fast Python package manager ([Installation Guide](https://github.com/astral-sh/uv))
- **Make**: Standard build automation tool
- **Docker** (Optional): For containerized deployments

---

## Usage

### 1. Installation
Install SOLA globally into your local environment:
```bash
make install
```

### 2. Authentication
Set your global OpenAI API key (stored securely in `~/.sola_config`):
```bash
sola auth
```

### 3. Initialize Project
Create a new standardized AI microservice structure:
```bash
sola init <project-name>
```

### 4. Forge Logic (The AI Architect)
Generate specialized business logic into `app/services.py`:
```bash
sola build --task "extract legal entities from contract documents using GPT-4o"
```

---

## Roadmap & TODO (MVP)
- [x] **Core CLI Engine**: Powered by Typer + Rich.
- [x] **Infrastructure Scaffolding**: Modular `app/` and `tests/` generation via `sola init`.
- [x] **Global Authentication**: Secure API key storage via `sola auth`.
- [x] **AI Architect**: Autonomous logic generation into `services.py` via `sola build`.
- [x] **Linting & Formatting**: Integrate `Ruff` into generated projects for strict code quality.
- [x] **CI/CD Templates**: Automatic GitHub Actions (`ci.yml`) generation.
- [ ] **Containerization**: Standard `Dockerfile` and `docker-compose.yml` templates.
- [ ] **AI Evaluation Integration**: Built-in support for DeepEval (AI-as-a-Judge) in test templates.
- [ ] **Strict Schema Support**: Leverage OpenAI `response_format` for 100% valid Pydantic models.
- [ ] **Spec-Driven Architecture**: Opinionated system prompts for industrial-grade code generation.
- [ ] **PyPI Readiness**: Package SOLA for `pip install` accessibility.

---

## Development
To prepare the development environment:
1.  Setup & Editable Install: `make dev`
2.  Run tests: `make test`
3.  Linting: `make lint`
