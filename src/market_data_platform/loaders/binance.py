"""Загрузчик данных с Binance."""

from market_data_platform.config.settings import settings


def build_klines_url(symbol: str | None = None) -> str:
    """Собрать URL для запроса свечей."""
    symbol = symbol or settings.default_symbol
    return f"{settings.binance_api_url}/klines?symbol={symbol}"


def main() -> None:
    print(build_klines_url())
    print(build_klines_url("ETHUSDT"))


if __name__ == "__main__":
    main()
