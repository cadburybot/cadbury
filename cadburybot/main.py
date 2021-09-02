import typer
from cadburybot.commands import environments, requests

app = typer.Typer()
app.add_typer(environments.app, name="env", help="Manage environments in Cadbury")
app.add_typer(requests.app, name="request", help="Manage environments in Cadbury")


if __name__ == "__main__":
    app()
