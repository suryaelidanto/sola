import os
from pathlib import Path

import typer

from sola.core import TEMPLATE_DIR, console, render_file

app = typer.Typer()


@app.command()
def create_project(
    project_name: str = typer.Argument(..., help="Name of the project"),
):
    """
    Step 1: Scaffolding - Forge the professional infrastructure.
    """

    project_path = Path.cwd() / project_name

    console.print(
        f"[bold green]Forging architecture for:[/bold green] [cyan]{project_name}[/cyan]..."
    )

    try:
        directories = [
            "app/features/health",
            "app/shared",
            "test/evals",
            ".github/workflows",
        ]

        for folder in directories:
            os.makedirs(project_path / folder, exist_ok=True)
            if not folder.startswith("."):
                (project_path / folder / "__init__.py").touch()

        files = {
            "Makefile.j2": "Makefile",
            "README.md.j2": "README.md",
            "pyproject.toml.j2": "pyproject.toml",
            "main.py.j2": "app/main.py",
            "health_router.py.j2": "app/features/health/router.py",
            "Dockerfile.j2": "Dockerfile",
            "docker-compose.yml.j2": "docker-compose.yml",
        }

        context = {"project_name": project_name}

        for t_name, f_name in files.items():
            if (TEMPLATE_DIR / t_name).exists():
                render_file(t_name, project_path / f_name, context=context)
            else:
                console.print(f"[yellow]Skipping missing template:[/yellow] {t_name}")

        console.print(
            f"[bold green]Success![/bold green] Infrastructure ready at {project_path}"
        )

    except Exception as e:
        console.print(f"[bold red]Initiation failed:[/bold red] {str(e)}")
