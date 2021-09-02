import typer

from cadburybot.utils.file_factory import EnvironmentStore
from cadburybot.utils.echo import Echo

app = typer.Typer()


@app.command()
def create(name: str):
    authorization_header, base_url, protocol = ask_env_details_from_user()

    typer.secho("Creating Environment...", bold=True)
    new_env = {
        "protocol": protocol,
        "base_url": base_url,
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
    Echo.json(EnvironmentStore.read()[name])
    typer.secho("Environment created successfully!", fg="green", bold=True)


@app.command()
def get(name: str = typer.Argument(None), file: bool = typer.Option(False)):
    try:
        if name:
            Echo.json(EnvironmentStore.read()[name])
        else:
            if file:
                Echo.open_file(EnvironmentStore.file_name())
            else:
                Echo.json(EnvironmentStore.read())
    except FileNotFoundError:
        exit_no_env_file()
    except KeyError as name:
        exit_no_env(name)


@app.command()
def edit(name: str):
    try:
        environments = EnvironmentStore.read()
        current_env: dict = environments[name]
        authorization_header, base_url, protocol = ask_env_details_from_user(current_env)
        environments[name] = {
            "protocol": protocol,
            "base_url": base_url,
            "authorization_header": authorization_header
        }
        EnvironmentStore.write(environments)
        Echo.json(environments[name], msg="=> Environment updated successfully!")
    except FileNotFoundError:
        exit_no_env_file()
    except KeyError as name:
        exit_no_env(name)


@app.command()
def delete(name: str):
    try:
        environments = EnvironmentStore.read()
        del environments[name]
        Echo.json(environments, msg=f"Environment {name} deleted!")
    except FileNotFoundError:
        exit_no_env_file()
    except KeyError as name:
        exit_no_env(name)


def ask_env_details_from_user(env=None):
    if env:
        protocol = env["protocol"]
        base_url = env["base_url"]
        authorization_header = env["authorization_header"]
    else:
        protocol = "http"
        base_url = "localhost:3000"
        authorization_header = ""

    cadbury = typer.style("Cadbury", fg=typer.colors.BLUE, bold=True)
    typer.echo(f"=> Hi, I am {cadbury}.")
    typer.echo(
        "=> I am here to manage your API environments and make your development experience enjoyable!")
    protocol = typer.prompt("What is the protocol?", default=protocol)
    base_url = typer.prompt("What is the base url?", default=base_url)
    authorization_header = typer.prompt("What is the authorization header value? It looks something like this `Bearer "
                                        "<token>`",
                                        default=authorization_header,
                                        show_default=False)
    return authorization_header, base_url, protocol


def exit_no_env_file():
    command = typer.style("`cadbury env create <name>`", bold=True, fg="green")
    message = typer.style("You can create an environment using this command:", dim=True)
    typer.secho("=> 0 environments found!", bold=True)
    typer.secho(f"=> {message} {command}")
    exit()


def exit_no_env(name):
    typer.secho(f"=> Sorry! There is no environment with name {name}", bold=True, fg="red")
    typer.secho("Here are the names of the environments created by you...")
    typer.secho("- " + "\n- ".join(EnvironmentStore.read().keys()), bold=True)
    exit()