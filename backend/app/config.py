from pydantic import BaseModel
import os
from typing import Optional


class Settings(BaseModel):
    server_port: int = 8000
    server_host: str = "0.0.0.0"
    log_level: str = "INFO"


def load_config() -> Settings:
    """Load configuration with environment variables taking precedence over defaults"""
    settings = Settings()

    # Environment variables override defaults
    if os.getenv("SERVER_PORT"):
        try:
            settings.server_port = int(os.getenv("SERVER_PORT"))
        except ValueError:
            pass  # Keep default if invalid

    if os.getenv("SERVER_HOST"):
        settings.server_host = os.getenv("SERVER_HOST")

    if os.getenv("LOG_LEVEL"):
        log_level = os.getenv("LOG_LEVEL").upper()
        if log_level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            settings.log_level = log_level

    return settings


# Global settings instance
settings = load_config()
