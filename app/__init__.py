from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title="Workout API", docs_url="/api/docs")

    return app