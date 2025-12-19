from typing import TypedDict


# -------- get_real_time_stock_price --------


class StockQuote(TypedDict):
    symbol: str
    name: str
    price: float
    changePercentage: float
    change: float
    volume: int
    dayLow: float
    dayHigh: float
    yearLow: float
    yearHigh: float
    marketCap: int
    priceAvg50: float
    priceAvg200: float
    exchange: str
    open: float
    previousClose: float
    timestamp: int


