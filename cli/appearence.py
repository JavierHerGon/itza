import click
from pydantic import BaseModel
from enum import Enum

class DialogBox(BaseModel):
    reset: str = "\\e[0m"

    def info(self, msg: str):
        click.echo("(⌐■_■) -- " + click.style("INFO:", bold=True, fg='black', bg='blue') + "  " +msg)


    def todo(self, msg: str):
        click.echo("(⌐■_■) -- "  + click.style("INFO:", bold=True, fg='black', bg='red') + "  " +msg)

    @staticmethod
    def debug(self, msg:str):
        click.echo("(⌐■_■) -- "  + click.style("INFO:", bold=True, fg='black', bg='yellow') + "  " +msg)

    @staticmethod
    def error(self, msg: str):
        click.echo("(⌐■_■) -- "  + click.style("INFO:", bold=True, fg='black', bg='red') + "  " +msg)
