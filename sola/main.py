import typer

from sola.commands.auth import set_auth
from sola.commands.init import create_project
from sola.commands.build import generate_logic

app = typer.Typer(
    help="SOLA: Standardized Orchestration & Logic Architecture",
    add_completion=False,
    no_args_is_help=True,
)

app.command(name="auth")(set_auth)
app.command(name="init")(create_project)
app.command(name="build")(generate_logic)


if __name__ == "__main__":
    app()
