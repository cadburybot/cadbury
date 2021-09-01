import typer
import json


def dimmed_text(string: str):
    return typer.style(string, dim=True)


def echo_json(data: dict, msg="> There you go!"):
    json_data = json.dumps(data, indent=4)
    typer.secho(msg, bold=True)
    typer.secho(json_data)
