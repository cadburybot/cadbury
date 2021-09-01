import typer
import environments

app = typer.Typer()
app.add_typer(environments.app, name="env", help="Manage environments in Cadbury")


if __name__ == "__main__":
    app()
