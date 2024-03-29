from app.core.logger import logger
from app.factory import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting server (reload enabled) [http://localhost:8000]")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
