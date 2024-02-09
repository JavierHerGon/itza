from fastapi import FastAPI
import logging


app = FastAPI()
logging.basicConfig(
                level=logging.DEBUG,
                format="[%(asctime)s] %(levelname)s - %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p",
            )
logger = logging.getLogger(__name__)

#app.add_middleware(
#    PrometheusMiddleware,
#    group_paths=True,
#    app_name=APP_NAME,
#    filter_unhandled_paths=True,
#)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/greet")
async def root():
    logger.info("Finally!")
    return {"status": "ok"}


app = FastAPI()

if __name__ == '__main__':
    import uvicorn
    print("Hello (⌐■_■)")
    uvicorn.run("app:app", port=8080, reload=True, log_level="info")
