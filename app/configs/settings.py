from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = Field(dafault="postgresql+asyncpg://postgres:postgres@postgres:5432/workoutapi")

settings = Settings()