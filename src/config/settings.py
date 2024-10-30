from enum import Enum
from functools import lru_cache
from typing import Any

from pydantic import BaseSettings, Field


class LogLevels(str, Enum):
    """Enum of permitted log levels."""

    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"
    critical = "critical"


class UvicornSettings():
    """Settings for uvicorn server"""

    host: str
    port: int = Field(ge=0, le=65535)
    log_level: LogLevels
    reload: bool


class ApiConfigSettings(BaseSettings):
    """Settings for FastAPI Server"""

    title: str = ""
    description: str = ""
    version: str
    docs_url: str

class Settings():
    uvicorn: UvicornSettings
    api_config: ApiConfigSettings
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


# def load_from_yaml() -> Any:
#     with open("appsettings.yaml") as fp:
#         config = yaml.safe_load(fp)
#     return config


@lru_cache()
def get_settings() -> Settings:
    # yaml_config = load_from_yaml()
    settings = Settings()
    uvicorn = UvicornSettings()
    uvicorn.host =  "0.0.0.0"
    uvicorn.log_level =  "info"
    uvicorn.reload = 0
    uvicorn.port =  8000

    settings.uvicorn = uvicorn
    settings.ACCESS_TOKEN_EXPIRE_MINUTES = 30
    settings.SECRET_KEY = "your-secret-key"
    settings.ALGORITHM = "HS256"
    return settings
