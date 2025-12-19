from typing import TypedDict

class CompanyPeer(TypedDict):
    symbol: str
    companyName: str
    price: float
    mktCap: int


class CompanySearchResult(TypedDict):
    symbol: str
    name: str
    currency: str
    exchangeFullName: str
    exchange: str


class CompanyProfile(TypedDict):
    symbol: str
    price: float
    marketCap: int
    beta: float
    lastDividend: float
    range: str
    change: float
    changePercentage: float
    volume: int
    averageVolume: int
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchangeFullName: str
    exchange: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    fullTimeEmployees: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    image: str
    ipoDate: str
    defaultImage: bool
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool
