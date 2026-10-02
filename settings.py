from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

# Base Settings
class Settings(BaseSettings):
    DB_CONNECTION_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    EXPIRY: float

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

@lru_cache()
def get_settings():
    return Settings()   # type: ignore

# Instance of Settings
settings: Settings = get_settings()