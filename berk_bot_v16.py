import ccxt
import os
import time
from dotenv import load_dotenv

load_dotenv()
exchange = ccxt.binance({'apiKey': os.getenv('API_KEY'), 'secret': os.getenv('API_SECRET'), 'options': {'defaultType': 'future'}})

def run():
    print("Bot basladi.")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    run()
