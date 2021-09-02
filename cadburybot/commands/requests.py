import typer

from cadburybot.utils.file_factory import EnvironmentStore
from cadburybot.utils.echo import Echo

app = typer.Typer()

#
# @app.command()
# def create(name: str):
#     authorization_header, base_url = ask_env_details_from_user()
#
#     typer.secho("Creating Environment...", bold=True)
#     new_env = {
#         "base_url": base_url,
#         "authorization_header": authorization_header
#     }
#     try:
#         environments: dict = EnvironmentStore.read()
#         environments[name] = new_env
#     except FileNotFoundError:
#         environments = {
#             name: new_env
#         }
#
#     EnvironmentStore.write(environments)
#     Echo.json(EnvironmentStore.read()[name])
#     typer.secho("Environment created successfully!", fg="green", bold=True)
#
#
# @app.command()
# def get(name: str = typer.Argument(None)):
#     try:
#         if name:
#             Echo.json(EnvironmentStore.read()[name])
#         else:
#             Echo.json(EnvironmentStore.read())
#     except FileNotFoundError:
#         exit_no_env_found()
#
#
# @app.command()
# def edit(name: str):
#     try:
#         environments = EnvironmentStore.read()
#         current_env: dict = environments[name]
#         authorization_header, base_url = ask_env_details_from_user(current_env)
#
#         typer.secho("Updating Environment...", bold=True)
#         environments[name] = {
#             "base_url": base_url,
#             "authorization_header": authorization_header
#         }
#         EnvironmentStore.write(environments)
#         typer.secho("Environment updated successfully!", fg="green", bold=True)
#     except FileNotFoundError:
#         exit_no_env_found()
#     except KeyError as name:
#         typer.secho(f"=> Sorry! There is no environment with name {name}", bold=True, fg="red")
#         typer.secho("Here are the names of the environments created by you...")
#         typer.secho("\n".join(EnvironmentStore.read().keys()), bold=True)
#         exit()
#
#
# @app.command()
# def delete(name: str):
#     try:
#         Echo.json(EnvironmentStore.read()[name])
#     except FileNotFoundError:
#         exit_no_env_found()
#     except KeyError as name:
#         typer.secho(f"=> Sorry! There is no environment with name {name}", bold=True, fg="red")
#         typer.secho("Here are the names of the environments created by you...")
#         typer.secho("\n".join(EnvironmentStore.read().keys()), bold=True)
#         exit()
#
#
# def ask_env_details_from_user(env=None):
#     if env:
#         base_url = env["base_url"]
#         authorization_header = env["authorization_header"]
#     else:
#         base_url = "localhost"
#         authorization_header = ""
#
#     cadbury = typer.style("Cadbury", fg=typer.colors.GREEN, bold=True)
#     typer.echo(f"=> Hi, I am {cadbury}.")
#     typer.echo(
#         "=> I am here to manage your API environments and make your development experience enjoyable!")
#     typer.echo("=> You can create an environment by following the prompts\n")
#     base_url = typer.prompt("What is the base url?", default=base_url)
#     authorization_header = typer.prompt("What is the authorization header value? It looks something like this `Bearer "
#                                         "<token>`",
#                                         default=authorization_header,
#                                         show_default=False)
#     return authorization_header, base_url
#
#
# def exit_no_env_found():
#     command = typer.style("`cadbury env create <name>`", bold=True, fg="green")
#     message = typer.style("You can create an environment using this command:", dim=True)
#     typer.secho("=> 0 environments found!", bold=True)
#     typer.secho(f"=> {message} {command}")
#     exit()
