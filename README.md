# SOLA: Standardized Orchestration & Logic Architecture

![CI Status](https://github.com/suryaelidanto/sola/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

SOLA is an opinionated CLI tool designed for AI Engineers to scaffold production-ready microservices. It enforces clean architecture, standardized infrastructure, and leverages LLMs for autonomous business logic generation.

## Core Philosophy
1.  **Architecture over Boilerplate:** Every project starts with a modular, enterprise-ready structure.
## The "Golden Stack" (Opinionated)
SOLA doesn't ask "what do you want?". It gives you what works in production:
*   **Framework**: `FastAPI` (Async)
*   **LLM Ops**: `AsyncOpenAI` (Native Structured Outputs)
*   **Validation**: `Pydantic V2` (Strict Schemas)
*   **Quality**: `DeepEval` (AI-as-a-Judge Testing)
*   **Packaging**: `uv` (The fastest package manager)
*   **Architecture**: **Vertical Slices** (Feature-based folder structure)

---

## Quick Start
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

## Roadmap & TODO (The "Industrial Grade" MVP)
We are pausing on content creation to ensure the MVP is truly production-ready.

### 1. Context-Aware Architecture (The "Brain")
- [ ] **Project Memory (`.sola/context.md`)**:
    - [ ] Create a persistent context file during `sola init`.
    - [ ] **Self-Learning Loop**: Every `sola build` updates this memory with the new feature's summary.
    - [ ] **Smart Context Injection**: `sola build` reads existing `SCHEMAS` and `ROUTERS` to avoid duplication and encourage reuse.
- [ ] **Spec-Driven Prompts**: The AI currently reads `specs/ARCHITECTURE.md` and `specs/AI_ENGINEERING.md`. Next step is ensuring it *strictly* obeys them via validation.

### 2. Full Vertical Slice Generation (The "Builder")
Currently `sola build` outputs a single file. The MVP target is to generate the **Entire Slice**:
- [ ] **Multi-File Generation**:
    - `app/features/{feature_name}/router.py` (FastAPI Endpoints)
    - `app/features/{feature_name}/schemas.py` (Pydantic Models)
    - `app/features/{feature_name}/service.py` (Business Logic)
    - `app/features/{feature_name}/__init__.py` (Package marker)
- [ ] **Auto-Registration**: Automatically import and register the new router in `app/main.py` using AST manipulation or regex.

### 3. Standards & Quality Gates
- [x] **Linting & Formatting**: Integrate `Ruff` into generated projects.
- [x] **CI/CD Templates**: Automatic GitHub Actions (`ci.yml`).
- [x] **Architecture Specifications**: Validated Vertical Slice Architecture standards.
- [ ] **Containerization**: Standard `Dockerfile` and `docker-compose.yml` templates.
- [ ] **AI Evaluation Integration**: Built-in support for `DeepEval` (AI-as-a-Judge) in test templates.
- [ ] **Strict Schema Support**: Leverage OpenAI `response_format` for 100% valid Pydantic models.
- [ ] **PyPI Readiness**: Package SOLA for `pip install` accessibility.

---

## Development
To prepare the development environment:
1.  Setup & Editable Install: `make dev`
2.  Run tests: `make test`
3.  Linting: `make lint`
