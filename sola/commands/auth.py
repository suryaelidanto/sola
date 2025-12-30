from pathlib import Path

import typer

from sola.core import console

app = typer.Typer()


@app.command(name="auth")
def set_auth(
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
