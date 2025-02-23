import json
import os


class Config:
    _path: str | None
    _json_config: dict | None

    # implement global configuration and environment configuration
    preserve_responses: bool

    def __init__(self, path: str | None = None):
        if not path:
            if os.name == "nt":
                self._path = os.path.join(
                    os.path.expanduser("~"), "AppData", "Local", "lazycurl"
                )
            elif os.name == "posix":
                self._path = os.path.join(
                    os.path.expanduser("~"), ".config", "lazycurl"
                )
            else:
                self._path = os.path.join(os.path.expanduser("~"), "lazycurl")

        self._json_config = self.read_config(self._path)

    def read_config(self, path: str) -> dict | None:
        if not os.path.exists(path):
            os.makedirs(path)
            return None
        else:
            with open(os.path.join(path, "config.json"), "r") as f:
                return json.load(f)

    def parse_config(self) -> None:
        self.preserve_responses = self._json_config.get("preserve_responses", True)
