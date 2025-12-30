from sola.main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app_version():
    """Simple smoke test for the CLI."""
    # This assumes there is a version command or at least the app starts
    # If no command exists yet, this might fail, but it's a start.
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
