import os
import subprocess
import sys
from typing import Any

import typer
import json


class Echo:
    @staticmethod
    def json(data: dict, msg: Any = "> There you go!"):
        json_data = json.dumps(data, indent=4)
        Echo.divider()
        typer.secho(msg, bold=True, fg="green")
        Echo.divider()
        typer.secho(json_data)
        Echo.divider()

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
    def dimmed(string: str):
        typer.secho(string, dim=True)
