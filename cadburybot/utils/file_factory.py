import json
import os
from pathlib import Path

from cadburybot.utils.echo import Echo

CONFIG_DIR = f"{str(Path.home())}/cadburybot"
ENV_FILE = f"{CONFIG_DIR}/environments.json"
CONFIGS_FILE = f"{CONFIG_DIR}/configs.json"


class FileFactory:
    @staticmethod
    def write_json(data: dict, file_name: str):
        json_object = json.dumps(data, indent=4)
        with open(file_name, "w") as outfile:
            outfile.write(json_object)

    @staticmethod
    def read_json(file_name: str) -> dict:
        with open(file_name, 'r') as openfile:
            return json.load(openfile)


class EnvironmentStore:
    @staticmethod
    def is_env_created() -> bool:
        path = Path(CONFIGS_FILE)
        return path.is_file()

    @staticmethod
    def is_default_config_set() -> str:
        return ENV_FILE

    @staticmethod
    def file_name() -> str:
        return ENV_FILE

    @staticmethod
    def read() -> dict:
        return FileFactory.read_json(file_name=ENV_FILE)

    @staticmethod
    def write(data: dict):
        os.makedirs(os.path.dirname(ENV_FILE), exist_ok=True)
        FileFactory.write_json(data, file_name=ENV_FILE)

    @staticmethod
    def set_as_default(name: str) -> bool:
        try:
            configs = FileFactory.read_json(CONFIGS_FILE)
            configs["default_env"] = name
            FileFactory.write_json(configs, file_name=CONFIGS_FILE)
            return True
        except FileNotFoundError:
            os.makedirs(os.path.dirname(CONFIGS_FILE), exist_ok=True)
            FileFactory.write_json({"default_env": name}, file_name=CONFIGS_FILE)
            return False

    @staticmethod
    def get_default() -> str:
        try:
            return FileFactory.read_json(CONFIGS_FILE)["default_env"]
        except Exception as e:
            Echo.error(e)
