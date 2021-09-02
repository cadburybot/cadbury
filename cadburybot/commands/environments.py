import typer

from cadburybot.utils.echo import Echo
from cadburybot.utils.file_factory import EnvironmentStore

app = typer.Typer()


@app.command()
def create(name: str):
    authorization_header, base_url, is_default = ask_env_details_from_user()

    typer.secho("Creating Environment...", bold=True)
    new_env = {
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
    if is_default:
        EnvironmentStore.set_as_default(name)
    Echo.json({name: EnvironmentStore.read()[name]})


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
        authorization_header, base_url, is_default = ask_env_details_from_user(current_env)
        environments[name] = {
            "base_url": base_url,
            "authorization_header": authorization_header
        }
        EnvironmentStore.write(environments)
        if is_default:
            EnvironmentStore.set_as_default(name)
        Echo.json(environments[name])
    except FileNotFoundError:
        exit_no_env_file()
    except KeyError as name:
        exit_no_env(name)


@app.command()
def delete(name: str):
    try:
        environments = EnvironmentStore.read()
        del environments[name]
        EnvironmentStore.write(environments)
        Echo.info(f"Environment {typer.style(name, fg=typer.colors.BRIGHT_BLUE)} deleted!")
    except FileNotFoundError:
        exit_no_env_file()
    except KeyError as name:
        exit_no_env(name)


def ask_env_details_from_user(env=None):
    if env:
        base_url = env["base_url"]
        authorization_header = env["authorization_header"]
    else:
        base_url = "http://localhost:3000"
        authorization_header = ""

    cadbury = typer.style("Cadbury", fg=typer.colors.BLUE, bold=True)
    typer.echo(f"> Hi, I am {cadbury}.")
    typer.echo(
        "> I am here to manage your API environments and make your API experience simple!")
    Echo.divider()
    base_url = typer.prompt("What is the base url?", default=base_url)
    authorization_header = typer.prompt("What is the authorization header value? It looks something like this `Bearer "
                                        "<token>`",
                                        default=authorization_header,
                                        show_default=False)
    is_default = typer.confirm("Do you want this to be your default environment?", default=True)
    return authorization_header, base_url, is_default


def exit_no_env_file():
    command = typer.style("`cadbury env create <name>`", bold=True, fg="green")
    message = typer.style("You can create an environment using this command:", dim=True)
    typer.secho("> 0 environments found!", bold=True)
    typer.secho(f"> {message} {command}")
    exit()


def exit_no_env(name):
    typer.secho(f"> Sorry! There is no environment with name {name}", bold=True, fg="red")
    typer.secho("Here are the names of the environments created by you...")
    typer.secho("- " + "\n- ".join(EnvironmentStore.read().keys()), bold=True)
    exit()
