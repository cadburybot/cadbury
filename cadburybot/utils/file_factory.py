import json
import os
from pathlib import Path

CONFIG_DIR = f"{str(Path.home())}/cadburybot"
ENV_FILE = f"{CONFIG_DIR}/environments.json"


class FileFactory:
    @staticmethod
    def write(data: dict, file_name: str):
        json_object = json.dumps(data, indent=4)
        with open(file_name, "w") as outfile:
            outfile.write(json_object)

    @staticmethod
    def read(file_name: str) -> dict:
        with open(file_name, 'r') as openfile:
            return json.load(openfile)


class EnvironmentStore:
    @staticmethod
    def read() -> dict:
        return FileFactory.read(file_name=ENV_FILE)

    @staticmethod
    def write(data: dict):
        os.makedirs(os.path.dirname(ENV_FILE), exist_ok=True)
        FileFactory.write(data, file_name=ENV_FILE)
