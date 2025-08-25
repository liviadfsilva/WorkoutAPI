from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title="Workout API")

    return app