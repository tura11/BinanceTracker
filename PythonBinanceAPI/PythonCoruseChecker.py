import time
from binance import Client
from dotenv import load_dotenv
import os
import pandas as pd

# Wczytaj API Key i Secret Key z pliku .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# Inicjalizacja klienta Binance
client = Client(API_KEY, SECRET_KEY)

# Lista symboli do sprawdzania
symbols = ["BTCUSDT", "XRPUSDT", "ADAUSDT", "BNBUSDT", "ETHUSDT"]

def get_current_price(*symbols):
    prices = {}  # Słownik na ceny
    for symbol in symbols:
        try:
            ticker = client.get_symbol_ticker(symbol=symbol)
            prices[symbol] = float(ticker['price'])  # Konwersja ceny na float
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
    return prices  # Zwracamy słownik z cenami


while True:
    current_prices = get_current_price(*symbols)

    # Tworzymy DataFrame z cenami
    df = pd.DataFrame(list(current_prices.items()), columns=['Symbol', "Price"])

    # Zapisujemy do pliku CSV (nadpisanie pliku)
    df.to_csv("prices.csv", index=False)

    # Wyświetlamy ceny na ekranie
    for symbol, price in current_prices.items():
        print(f"Current price of {symbol}: {price}$")
    
    # Czekamy 60 sekund
    time.sleep(60)
