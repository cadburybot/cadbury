import json
import os
import subprocess
import sys
from typing import Any

import typer

PREFIX = typer.style("> ", fg=typer.colors.BRIGHT_YELLOW)


class Echo:
    @staticmethod
    def json(data: dict, divider=False, dim=False):
        if divider:
            Echo.divider()
        json_data = json.dumps(data, indent=4)
        typer.secho(json_data, dim=dim)
        if divider:
            Echo.divider()

    @staticmethod
    def info(msg: Any):
        typer.secho(f"{PREFIX} {msg}", bold=True)

    @staticmethod
    def error(string: Any):
        typer.secho(f"{PREFIX} {string}", fg="red", bold=True)

    @staticmethod
    def open_file(filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            subprocess.call(["less", filename])

    @staticmethod
    def divider():
        typer.secho(".....................................", dim=True)

    @staticmethod
    def prefix_start():
        return typer.style(">", fg=typer.colors.YELLOW)

    @staticmethod
    def prefix_mid():
        return typer.style("|", fg=typer.colors.YELLOW)

    @staticmethod
    def prefix_end():
        return typer.style("|_", fg=typer.colors.YELLOW)

    @staticmethod
    def dimmed(string: str):
        typer.secho(string, dim=True)
