from ..utils.utils import init_fmp_request, with_compound_tools
from ..models import *
from typing import List
import asyncio


request = init_fmp_request()


async def get_real_time_stock_price(symbol: str) -> StockQuote:
  """
  Description:
    Get the real-time stock price for a given symbol.
  Input:
    A stock symbol (e.g., "AAPL" for Apple Inc.).
  Output:
    A JSON array containing a dictionary with the following fields:
    - symbol (str): The stock ticker symbol.
    - name (str): Full company name.
    - price (float): Current stock price in USD.
    - changePercentage (float): Percentage change since previous close.
    - change (float): Absolute price change since previous close.
    - volume (int): Number of shares traded during the current trading session.
    - dayLow (float): Lowest price of the stock for the current day.
    - dayHigh (float): Highest price of the stock for the current day.
    - yearLow (float): Lowest price of the stock in the past 52 weeks.
    - yearHigh (float): Highest price of the stock in the past 52 weeks.
    - marketCap (int): Market capitalization in USD.
    - priceAvg50 (float): 50-day moving average price.
    - priceAvg200 (float): 200-day moving average price.
    - exchange (str): Stock exchange where the stock is listed.
    - open (float): Opening price of the stock for the current day.
    - previousClose (float): Closing price of the stock from the previous trading day.
    - timestamp (int): UNIX timestamp representing the time of the data.
  """
  try:
    response = request.get("/quote", params={"symbol": symbol})
    quotes = response.json()
    return quotes[0] if quotes else None
  except Exception as e:
    print(e)
    return {"error": str(e)}


async def get_stock_peers(symbol: str) -> List[CompanyPeer]:
  """
  Description:
    Get a list of peer companies for a given stock symbol.
  Input:
    A stock symbol (e.g., "AAPL" for Apple Inc.).
  Output:
    A JSON array containing a dictionary with the following fields:
    - symbol (str): The stock ticker symbol.
    - companyName (str): The full name of the company.
    - price (float): The current stock price in USD.
    - mktCap (int): The market capitalization of the company in USD.
  """
  try:
    response = request.get("/stock-peers", params={"symbol": symbol})
    return response.json()
  except Exception as e:
    print(e)
    return {"error": str(e)}


async def get_company_profile(symbol: str) -> CompanyProfile:
  """
  Description:
    Fetches detailed company profile information for a given stock symbol. 
  Input:
    symbol (str): The stock ticker symbol, e.g., "AAPL".
  Output:
    A JSON array containing a dictionary with the following fields:
    - symbol (str): Stock ticker symbol.
    - price (float): Current stock price in USD.
    - marketCap (int): Market capitalization in USD.
    - beta (float): Beta value of the stock.
    - lastDividend (float): Most recent dividend paid.
    - range (str): 52-week price range.
    - change (float): Price change since previous close.
    - changePercentage (float): Percentage price change since previous close.
    - volume (int): Shares traded during the session.
    - averageVolume (int): Average trading volume.
    - companyName (str): Full company name.
    - currency (str): Currency of the stock price.
    - cik (str): Central Index Key.
    - isin (str): International Securities Identification Number.
    - cusip (str): Committee on Uniform Securities Identification Procedures ID.
    - exchangeFullName (str): Full name of the exchange.
    - exchange (str): Short exchange symbol.
    - industry (str): Industry classification.
    - website (str): Company website URL.
    - description (str): Detailed description of the company.
    - ceo (str): CEO name.
    - sector (str): Sector of the company.
    - country (str): Headquarters country.
    - fullTimeEmployees (str): Number of full-time employees.
    - phone (str): Company contact phone number.
    - address (str): Street address of headquarters.
    - city (str): Headquarters city.
    - state (str): Headquarters state.
    - zip (str): Postal code.
    - image (str): URL to company logo/image.
    - ipoDate (str): IPO date in YYYY-MM-DD format.
    - defaultImage (bool): Whether a default image is used.
    - isEtf (bool): True if the stock is an ETF.
    - isActivelyTrading (bool): True if the stock is actively trading.
    - isAdr (bool): True if the stock is an ADR.
    - isFund (bool): True if the stock is a fund.
  """
  try:
    response = request.get("/profile", params={"symbol": symbol})
    profiles = response.json()
    return profiles[0] if profiles else None
  except Exception as e:
    print(e)
    return {"error": str(e)}


async def get_market_status(exchange: str) -> List[MarketHours]:
  """
  Description:
    Fetches the current market status for a given stock exchange.
  Input:
    exchange (str): The stock exchange symbol, e.g., "NASDAQ".
  Output:
    A JSON containing a dictionary with the following fields:
    - exchange (str): Exchange symbol.
    - name (str): Full name of the exchange.
    - openingHour (str): Exchange opening hours with timezone offset.
    - closingHour (str): Exchange closing hours with timezone offset.
    - timezone (str): Timezone of the exchange.
    - isMarketOpen (bool): True if the market is currently open, False otherwise.
  """
  try:
    response = request.get("/exchange-market-hours", params={"exchange": exchange})
    exchanges = response.json()
    return exchanges[0] if exchanges else None
  except Exception as e:
    print(e)
    return {"error": str(e)}


async def get_all_market_status() -> List[MarketHours]:
  """
  Description:
    Fetches the current market status of all the stock exchanges.
  Output:
    A JSON array containing a dictionary with the following fields:
    - exchange (str): Exchange symbol.
    - name (str): Full name of the exchange.
    - openingHour (str): Exchange opening hours with timezone offset.
    - closingHour (str): Exchange closing hours with timezone offset.
    - timezone (str): Timezone of the exchange.
    - isMarketOpen (bool): True if the market is currently open, False otherwise.
  """
  try:
    response = request.get("/all-exchange-market-hours")
    return response.json()
  except Exception as e:
    print(e)
    return {"error": str(e)}


async def search_company_name(company_name: str) -> List[CompanySearchResult]:
  """
  Description:
    Searches for companies matching the given name and returns a list of matching company details. You can use this tool to identify the company symbols.
  Input:
    company_name (str): The name or partial name of the company to search for.
  Output:
    A JSON array containing a dictionary with the following fields:
    - symbol (str): Stock ticker symbol.
    - name (str): Full company name.
    - currency (str): Currency in which the stock is traded.
    - exchangeFullName (str): Full name of the exchange.
    - exchange (str): Short symbol of the exchange.
  """
  try:
    response = request.get("/search-name", params={"query": company_name, "limit": 5})
    return response.json()
  except Exception as e:
    print(e)
    return {"error": str(e)}


async def analyze_stock_competitors(symbol: str):
    """
  Description:
    Analyzes given symbol current stock data and its competitors stock data.
  Input:
    symbol (str): The stock ticker symbol, e.g., "AAPL".
  Output:
    A dictionary containing:
    - symbol (str): The input stock symbol.
    - real_time_stock_price (List[StockQuote]): Real-time stock price data for the input symbol.
    - competitors_data (List[CompanyPeer]): List of peer companies for the input symbol.
    - competitor_profiles (Dict[str, List[CompanyProfile]]): Profiles of the top 3 peer companies.
  """
    try:
        real_time_stock_price_data, competitors_data = await asyncio.gather(
      get_real_time_stock_price(symbol), get_stock_peers(symbol)
    )

        peers = competitors_data[:3]
        profile_tasks = [(get_company_profile(peer["symbol"])) for peer in peers]
        competitor_profiles = await asyncio.gather(*profile_tasks)

        output = {
      "symbol": symbol,
      "real_time_stock_price": real_time_stock_price_data,
      "competitors_data": competitors_data,
      "competitor_profiles": {
        peer["symbol"]: profile for peer, profile in zip(peers, competitor_profiles)
      },
    } 
        return output
    except Exception as e:
        print(e)
        return {"error": str(e)}


fmp_tools = with_compound_tools(
    [
        get_real_time_stock_price,
        get_stock_peers,
        get_company_profile,
        get_market_status,
        get_all_market_status,
        search_company_name,
        analyze_stock_competitors,
    ]
)
