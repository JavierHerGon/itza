import click
from appearence import DialogBox
import requests

HOST = "localhost:8000"

promp = DialogBox()


@click.command()
@click.argument("action")
@click.argument("entity", required=False)
def main(action: str, entity: str):
    promp.info("Ahoi my son")

    r = requests.post(f"http://{HOST}/{action}/{entity}")
    return r.json()


if __name__ == "__main__":
    main()
