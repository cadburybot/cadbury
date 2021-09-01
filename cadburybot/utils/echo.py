import typer
import json


def dimmed_text(string: str):
    return typer.style(string, dim=True)


def echo_json(data: dict):
    json_data = json.dumps(data, indent=4)
    typer.secho(json_data, bold=True)
