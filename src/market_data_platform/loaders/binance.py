"""Загрузчик данных с Binance."""

import logging
import httpx
from market_data_platform.config.settings import settings

logger = logging.getLogger(__name__)


def build_klines_url(
        symbol: str | None = None, 
        interval: str | None = None,
        limit: int | None = None
        ) -> str:
    """Собрать URL для запроса свечей."""
    symbol = symbol or settings.default_symbol
    interval = interval or settings.default_interval
    limit = limit or settings.default_limit
    if limit > 1000:
        limit = 1000
        logger.warning("превышен лимит для данных свечей для %s. лимит обрезан до 1000", symbol)
    logger.debug("собираю URL для %s", symbol)
    url = f"{settings.binance_api_url}/klines?symbol={symbol}&interval={interval}&limit={limit}"
    logger.info("URL готов: %s", url)
    return url


def fetch_klines(
        url: str | None = None, 
        timeout: float | None = None,
        max_attempts: int | None = None
        ) -> int:
    """Get-запрос по заданному url с таймаутом"""
    url = url or settings.binance_api_url
    timeout = timeout or settings.request_timeout
    max_attempts = max_attempts or settings.request_attempts

    for attempt in range(1, max_attempts + 1):
        try:
            r = httpx.get(url=url, timeout=timeout)
            if r.status_code // 100 == 5:
                logger.warning("Ошибка соединения %s на попытке подключения #%s", r.status_code, attempt)
            else:
                return r.status_code
        except (httpx.TimeoutException, httpx.ConnectError) as e:
            logger.warning("Возникла сетевая ошибка %s на попытке подключения #%s", e, attempt)
            if attempt == max_attempts:
                raise
    return r.status_code


def main() -> None:
    from market_data_platform.config.logging import setup_logging

    setup_logging(settings.log_level)
    build_klines_url()
    url = build_klines_url("ETHUSDT")
    status = fetch_klines(url)
    # status = fetch_klines(url, timeout=0.001, max_attempts=3) # test TimeoutException
    # status = fetch_klines("https://httpbin.org/status/503", max_attempts=3) #test 503
    logger.info("статус ответа: %s", status)


if __name__ == "__main__":
    main()
