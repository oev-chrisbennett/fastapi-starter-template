from fastapi import FastAPI


def create_app():
    description = "Starter app template using FastAPI"
    app = FastAPI(
        title="FastAPI Starter",
        description=description,
        openapi_url="/api/openapi.json",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )

    return app
