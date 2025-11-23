import logging
import yaml

class Config:
    def __init__(self, config_path="config.yml"):
        self.LOG_LEVEL = logging.DEBUG
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def get_device(self, name):
        return self.config.get(name.upper())

config = Config()