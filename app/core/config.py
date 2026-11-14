from enum import StrEnum

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Environment(StrEnum):
    DEVELOPMENT = "development"
    TESTING = "test"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    app_name: str = "Project Name"
    app_env: Environment = Environment.DEVELOPMENT
    secret_key: SecretStr = SecretStr("")

    # Database
    database_url: SecretStr = SecretStr("")

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()
