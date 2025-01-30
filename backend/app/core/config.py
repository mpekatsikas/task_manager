from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@postgres:5432/postgres"
    SECRET_KEY: str = "secret"

    class Config:
        env_file = ".env"


settings = Settings()
