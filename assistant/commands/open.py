import logging
import webbrowser
from pydantic import BaseModel
from abc import ABC, abstractmethod
from enum import Enum
from config.settings import load_config
import subprocess

# TODO Better way to handle constants (settings with yaml)
COMMAND_TYPES = ("web", "app")
# TODO
config = load_config()

logger = logging.getLogger(__name__)


class EntityType(Enum):
    APP = 1
    WEB = 2


class OpenCommand(ABC, BaseModel):

    @classmethod
    def from_name(cls, name: str):
        match config[name]['type']:
            case EntityType.WEB.name:
                return OpenSite(**config[name])
            case EntityType.APP.name:
                return OpenApp(**config[name])

    @abstractmethod
    def open_entity(self):
        pass


class OpenSite(OpenCommand):
    name: str
    type: str
    url: str

    def open_entity(self):
        webbrowser.open(url=self.url)


class OpenApp(OpenCommand):
    name: str
    type: str
    path: str
    command: str = f"open -a"

    def open_entity(self):
        #TODO Not Working
        subprocess.run([f"{self.command} {self.path}.app"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
