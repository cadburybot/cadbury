from typing import Optional

import typer

from utils.file_factory import EnvironmentStore
from cadburybot.utils.echo import echo_json

app = typer.Typer()


@app.command()
def create(name: str):
    cadbury = typer.style("Cadbury", fg=typer.colors.GREEN, bold=True)
    typer.echo(f"=> Hi, I am {cadbury}.")
    typer.echo(
        "=> I am here to manage your API environments and make your development experience enjoyable!")
    typer.echo("=> You can create an environment by following the prompts\n")
    protocol = typer.prompt("What is the protocol?", default="http")
    base_url = typer.prompt("What is the base url?", default="localhost")
    port = typer.prompt("What is the port? (optional)", default=3000)
    authorization_header = typer.prompt("What is the authorization header value? It looks something like this `Bearer "
                                        "<token>`",
                                        default="",
                                        show_default=False)

    typer.secho("Creating Environment...", bold=True)
    new_env = {
        "protocol": protocol,
        "base_url": base_url,
        "port": port,
        "authorization_header": authorization_header
    }
    try:
        environments: dict = EnvironmentStore.read()
        environments[name] = new_env
    except FileNotFoundError:
        environments = {
            name: new_env
        }

    EnvironmentStore.write(environments)
    echo_json(EnvironmentStore.read()[name])
    typer.secho("Environment created successfully!", fg="green", bold=True)


@app.command()
def get(name: str = typer.Argument(None)):
    try:
        if name:
            echo_json(EnvironmentStore.read()[name])
        else:
            echo_json(EnvironmentStore.read())
    except FileNotFoundError:
        exit_no_env_found()


@app.command()
def edit(name: str):
    try:
        echo_json(EnvironmentStore.read()[name])
    except FileNotFoundError:
        exit_no_env_found()
    except KeyError as name:
        typer.secho(f"=> Sorry! There is no environment with name {name}", bold=True, fg="red")
        typer.secho("Here are the names of the environments created by you...")
        typer.secho("\n".join(EnvironmentStore.read().keys()), bold=True)
        exit()


def exit_no_env_found():
    command = typer.style("`cadbury env create <name>`", bold=True, fg="green")
    message = typer.style("You can create an environment using this command:", dim=True)
    typer.secho("=> 0 environments found!", bold=True)
    typer.secho(f"=> {message} {command}")
    exit()