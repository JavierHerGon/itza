import json

#TODO More elegant. maybe BaseSettings?
def load_config() -> (str, str):
    with open("../.secrets") as f:
        secrets = json.load(f)
    return secrets
