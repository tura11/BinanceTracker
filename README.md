# Binance Price Tracker

This project is a simple Python script that retrieves the current prices of selected cryptocurrencies from Binance and writes them to a CSV file every 60 seconds. It allows you to monitor price changes in near real-time.

## Features

- **Price Retrieval:** Uses the `python-binance` library to fetch current prices for specified trading pairs.
- **CSV Logging:** Saves the latest prices to a `prices.csv` file on every update cycle.
- **Real-time Monitoring:** Prints the current prices to the console for quick monitoring.
- **Automated Updates:** Continuously fetches updated prices at a 60-second interval.

## Requirements

- Python 3.x
- Libraries:
  - [python-binance](https://github.com/sammchardy/python-binance)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [pandas](https://pandas.pydata.org/)
- A Binance account with valid API Key and Secret Key.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
