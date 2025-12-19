from dotenv import load_dotenv
import os

load_dotenv()

FMP_URL = "https://financialmodelingprep.com/stable"

FMP_API_KEY = os.environ.get("FMP_API_KEY")
