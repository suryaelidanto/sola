import os
from pathlib import Path

import typer
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from rich.console import Console

load_dotenv()
console = Console()

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"
SPECS_DIR = BASE_DIR / "specs"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def render_file(template_name: str, target_path: Path, context: dict):
    """Renders a Jinja2 template with provided data."""
    template = env.get_template(template_name)
    content = template.render(context)
    target_path.write_text(content, encoding="utf-8")


def get_api_key() -> str:
    """
    Smart Retriever:
    1. Check Environment Variable (OPENAI_API_KEY)
    2. Check Global Config (~/.sola_config)
    3. Prompt User if missing
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


def get_sola_specs() -> str:
    """Reads the 'Constitution' (Architecture & Engineering Specs)."""

    arch_spec = (SPECS_DIR / "ARCHITECTURE.md").read_text(encoding="utf-8")
    eng_spec = (SPECS_DIR / "AI_ENGINEERING.md").read_text(encoding="utf-8")

    return f"""
    === SOLA ARCHITECTURE ===
    {arch_spec}

    === AI ENGINEERING STANDARDS ===
    {eng_spec}
    """
