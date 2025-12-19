from typing import TypedDict

class MarketHours(TypedDict):
    exchange: str
    name: str
    openingHour: str
    closingHour: str
    timezone: str
    isMarketOpen: bool

