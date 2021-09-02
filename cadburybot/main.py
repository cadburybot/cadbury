import typer

from cadburybot.commands import environments, requests
from cadburybot.utils.echo import Echo
from cadburybot.utils.file_factory import EnvironmentStore

app = typer.Typer()
app.add_typer(environments.app, name="env", help="Manage environments in Cadbury")
app.add_typer(requests.app, name="request", help="Manage environments in Cadbury")


@app.command()
def status():
    if not EnvironmentStore.is_env_created():
        no = typer.style('NO', bold=True)
        typer.secho(f"{Echo.prefix_start()} Hey, there are {no} environments found")
        create_env_cmd = typer.style("`cadbury env create <env-name>`", bold=True, fg="green")
        typer.secho(f"{Echo.prefix_end()} Try creating an environment using {create_env_cmd}")
        return

    current_env = typer.style(f"{EnvironmentStore.get_default()}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(f"\n{Echo.prefix_start()} Your current environment is {current_env}", bold=True)
    Echo.divider()
    typer.secho(f"\n{Echo.prefix_start()} Environments created by you", bold=True)
    for k, v in EnvironmentStore.read().items():
        req_count = 0
        if "requests" in v:
            req_count = len(v.keys())
        typer.secho(f"  |_ {k} ({req_count} requests)", dim=True)
    Echo.divider()


if __name__ == "__main__":
    app()
