# Imports and setup
import requests as req
import urllib3

# disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Pick a stock
ticker = input("Enter ticker: ")

# Get the data
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey=6C3GUKE8Z5C6Z2B5"
r = req.get(url, verify=False)
data = r.json()

# get the last refreshed date
last_refreshed = data["Meta Data"]["3. Last Refreshed"]

# get the closing price
closing_price = data["Time Series (5min)"][last_refreshed]["4. close"]

# Get the company overview
url_overview = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey=6C3GUKE8Z5C6Z2B5"
r = req.get(url_overview, verify=False)
data = r.json()

# get the company name
if "Name" in data:
    ticker_name = data["Name"]

# Results
try:
    print(f"Closing price of {ticker_name} on {last_refreshed} is {closing_price}")
except:
    print(f"Closing price of {ticker} on {last_refreshed} is {closing_price}")
