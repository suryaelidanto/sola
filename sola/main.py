import os
import typer
from pathlib import Path
from openai import AsyncOpenAI
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from rich.console import Console

load_dotenv()

app = typer.Typer(help="SOLA: Standardized Orchestration & Logic Architecture")
console = Console()

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def render_file(template_name: str, target_path: Path, context: dict):
    """Renders a Jinja2 template with provided data."""
    template = env.get_template(template_name)
    content = template.render(context)
    target_path.write_text(content)


def get_api_key() -> str:
    """
    Smart Retriever: Mencari di Environment Variable dulu, kalau tidak ada baru cari di file global .sola_config.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key.strip().strip('"').strip("'")

    config_file = Path.home() / ".sola_config"
    if config_file.exists():
        content = config_file.read_text().strip()
        return content.split("=")[-1].strip().strip('"').strip("'")

    console.print("[yellow]No API Key found. Let's set it up once![/yellow]")
    new_key = typer.prompt("Enter your OpenAI API Key", hide_input=True)

    config_file.write_text(f"OPENAI_API_KEY={new_key.strip()}")
    return new_key.strip().strip('"').strip("'")


@app.command()
def auth(
    api_key: str = typer.Option(
        ...,
        prompt="Set Global OpenAI API Key",
        hide_input=True,
        help="The OpenAI API key to store in your home directory",
    ),
):
    """
    Step 0: Authenticate - Store your API key globally for all project forging.
    """

    config_file = Path.home() / ".sola_config"
    config_file.write_text(f"OPENAI_API_KEY={api_key.strip()}")

    console.print(
        "[bold green]Authenticated![/bold green] Your key is stored globally at ~/.sola_config"
    )


@app.command()
def init(
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
        for folder in ["app", "tests"]:
            os.makedirs(project_path / folder, exist_ok=True)
            (project_path / folder / "__init__.py").touch()

        files = {
            "Makefile.j2": "Makefile",
            "README.md.j2": "README.md",
            "pyproject.toml.j2": "pyproject.toml",
        }

        context = {"project_name": project_name}

        for t_name, f_name in files.items():
            render_file(t_name, project_path / f_name, context=context)

        console.print(
            f"[bold green]Success![/bold green] Infrastructure ready at {project_path}"
        )

    except Exception as e:
        console.print(f"[bold red]Initiation failed:[/bold red] {str(e)}")


@app.command()
def build(
    task: str = typer.Option(..., "--task", "-t", help="Logic description"),
    project_dir: Path = typer.Option(Path.cwd(), help="Root directory of the project"),
):
    """
    Step 2: AI Architect - generate production-grade services.py via prompt.
    """

    async def _run_build():
        key = get_api_key()
        local_client = AsyncOpenAI(api_key=key)

        console.print(f"[bold yellow]Architecting logic for:[/bold yellow] {task}...")

        system_prompt = (
            "You are a Senior AI Backend Architect. Generate a clean, professional Python service. "
            "Standards: Use AsyncOpenAI, implement Pydantic V2 models, and use async def. "
            "Strict Rule: Return ONLY raw Python code. No markdown, no explanations, no chat."
        )

        user_prompt = f"Create specialized business logic for: {task}"

        try:
            response = await local_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.2,
            )
            generated_code = response.choices[0].message.content

            service_file = project_dir / "app" / "services.py"
            os.makedirs(service_file.parent, exist_ok=True)
            service_file.write_text(generated_code)

            console.print(
                "[bold green]Success![/bold green] Professional logic forged in app/services.py ☀️"
            )
        except Exception as e:
            console.print(f"[bold red]AI Architect failed:[/bold red] {str(e)}")

    import anyio

    anyio.run(_run_build)


if __name__ == "__main__":
    app()
