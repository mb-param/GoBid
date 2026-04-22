from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    app_port: int = 8000
    api_prefix: str = "/api/v1"
    frontend_origin: str = "http://localhost:5173"

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/gobid"
    jwt_secret: str = "change-me"

    openai_api_key: str = ""
    llm_model: str = "gpt-4o-mini"


@lru_cache
def get_settings() -> Settings:
    return Settings()
