"""Настройки приложения."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Конфигурация, читается из переменных окружения и .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    binance_api_url: str = "https://api.binance.com/api/v3"
    default_symbol: str = "BTCUSDT"
    default_interval: str = "1h"
    log_level: str = "INFO"
    request_timeout: float = 10.0

    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str


settings = Settings()
