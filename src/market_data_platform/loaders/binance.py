"""Загрузчик данных с Binance."""

from market_data_platform.config.settings import BINANCE_API_URL, DEFAULT_SYMBOL


def build_klines_url(symbol: str = DEFAULT_SYMBOL) -> str:
    """Собрать URL для запроса свечей."""
    return f"{BINANCE_API_URL}/klines?symbol={symbol}"


def main() -> None:
    print(build_klines_url())


if __name__ == "__main__":
    main()
