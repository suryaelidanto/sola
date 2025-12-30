import os
from pathlib import Path

import typer
from openai import AsyncOpenAI

from sola.core import console, get_api_key, get_sola_specs

app = typer.Typer()


@app.command()
def generate_logic(
    task: str = typer.Option(..., "--task", "-t", help="Logic description"),
    project_dir: Path = typer.Option(Path.cwd(), help="Root directory of the project"),
):
    """
    Step 2: AI Architect - generate production-grade services via prompt.
    """

    async def _run_build():
        sola_specs = get_sola_specs()

        key = get_api_key()
        local_client = AsyncOpenAI(api_key=key)

        console.print(f"[bold yellow]Architecting logic for:[/bold yellow] {task}...")

        system_prompt = (
            "You are a Senior AI Backend Architect strictly following SOLA standards.\n"
            f"{sola_specs}\n\n"
            "TASK: Generate a clean, professional Python service file (service.py).\n"
            "STRICT RULES:\n"
            "- Return ONLY raw Python code.\n"
            "- Implement Pydantic models for inputs/outputs.\n"
            "- Use 'instructor' with 'AsyncOpenAI' as per standards."
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
            generated_code = (
                generated_code.replace("```python", "").replace("```", "").strip()
            )

            service_file = project_dir / "app" / "services.py"
            os.makedirs(service_file.parent, exist_ok=True)
            service_file.write_text(generated_code)

            console.print(
                "[bold green]Success![/bold green] Professional logic forged in app/services.py"
            )
        except Exception as e:
            console.print(f"[bold red]AI Architect failed:[/bold red] {str(e)}")

    import anyio

    anyio.run(_run_build)
