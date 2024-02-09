from fastapi import FastAPI
import logging
from commands.open import OpenCommand

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
logger = logging.getLogger(__name__)


# app.add_middleware(
#    PrometheusMiddleware,
#    group_paths=True,
#    app_name=APP_NAME,
#    filter_unhandled_paths=True,
# )




@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/greet")
def greet():
    logger.warning("Finally! (⌐■_■)")
    return {"status": "pumped"}

@app.get("/items/{item_id}")
def get_item(item_id):
    return {'item_id': item_id}

@app.post("/open/{name}")
def open_entity(name: str):
    open_command = OpenCommand.from_name(name)
    open_command.open_entity()

    with open("../resources/ascii_art/bd.txt") as f:
        draw = f.readlines()
        return draw




if __name__ == '__main__':
    import uvicorn

    print("Hello (⌐■_■)")
    uvicorn.run("app:app", port=8000, reload=True, log_level="info")
