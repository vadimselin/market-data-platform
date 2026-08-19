"""Загрузчик данных с Binance."""

import logging

from market_data_platform.config.settings import settings

logger = logging.getLogger(__name__)


def build_klines_url(symbol: str | None = None) -> str:
    """Собрать URL для запроса свечей."""
    symbol = symbol or settings.default_symbol
    logger.debug("собираю URL для %s", symbol)
    url = f"{settings.binance_api_url}/klines?symbol={symbol}"
    logger.info("URL готов: %s", url)
    return url


def main() -> None:
    from market_data_platform.config.logging import setup_logging

    setup_logging(settings.log_level)
    build_klines_url()
    build_klines_url("ETHUSDT")


if __name__ == "__main__":
    main()
