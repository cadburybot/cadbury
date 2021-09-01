import typer

from utils.file_factory import EnvironmentStore
from cadburybot.utils.echo import echo_json

app = typer.Typer()


@app.command()
def create(name: str):
    cadbury = typer.style("Cadbury", fg=typer.colors.GREEN, bold=True)
    typer.echo(f"\nHi, I am {cadbury}.")
    typer.echo("I am here to manage your API environments and make your development experience enjoyable!\n")
    protocol = typer.prompt("What is the protocol?", default="http")
    base_url = typer.prompt("What is the base url?", default="localhost")
    port = typer.prompt("What is the port? (optional)", default=3000)
    authorization_header = typer.prompt("What is the authorization header value? It looks something like this `Bearer "
                                        "<token>`",
                                        default="",
                                        show_default=False)
    typer.secho("Creating Environment...", bold=True)
    EnvironmentStore.write({
        name: {
            "protocol": protocol,
            "base_url": base_url,
            "port": port,
            "authorization_header": authorization_header
        }
    })
    echo_json(EnvironmentStore.read())
    typer.secho("==> Environment created successfully!", fg="green", bold=True)

