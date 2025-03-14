import time
from binance import Client
from dotenv import load_dotenv
import os
import pandas as pd


load_dotenv()
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")


client = Client(API_KEY, SECRET_KEY)


symbols = ["BTCUSDT", "XRPUSDT", "ADAUSDT", "BNBUSDT", "ETHUSDT"]

def get_current_price(*symbols):
    prices = {} 
    for symbol in symbols:
        try:
            ticker = client.get_symbol_ticker(symbol=symbol)
            prices[symbol] = float(ticker['price']) 
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
    return prices 


while True:
    current_prices = get_current_price(*symbols)

  
    df = pd.DataFrame(list(current_prices.items()), columns=['Symbol', "Price"])

  
    df.to_csv("prices.csv", index=False)

  
    for symbol, price in current_prices.items():
        print(f"Current price of {symbol}: {price}$")
    
  
    time.sleep(60)
