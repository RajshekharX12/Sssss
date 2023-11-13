import time
import requests
from pyrogram import Client

# Your Telegram Bot Token
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Your Telegram Channel ID (replace with your channel ID)
CHANNEL_ID = -100123456789

# Abstract API URL for exchange rates
ABSTRACT_API_URL = "https://exchange-rates.abstractapi.com/v1/live"

# Your Abstract API Key
ABSTRACT_API_KEY = "YOUR_ABSTRACT_API_KEY"

# Function to get exchange rates
def get_exchange_rate():
    try:
        response = requests.get(f"{ABSTRACT_API_URL}/?api_key={ABSTRACT_API_KEY}&base=USD&target=EUR")
        data = response.json()
        exchange_rate = data["exchange_rates"]["EUR"]
        return f"Bitcoin Exchange Rate: 1 BTC = {exchange_rate} EUR"
    except Exception as e:
        print(f"Error getting Bitcoin exchange rate: {e}")
        return None

# Pyrogram client setup
app = Client(
    "bitcoin_price_bot",
    bot_token=BOT_TOKEN,
)

# Function to update channel description
def update_channel_description():
    exchange_rate = get_exchange_rate()
    if exchange_rate:
        try:
            app.set_chat_description(CHANNEL_ID, exchange_rate)
            print(f"Channel description updated: {exchange_rate}")
        except Exception as e:
            print(f"Error updating channel description: {e}")

# Main loop to update every 5 minutes
while True:
    update_channel_description()
    time.sleep(300)  # 5 minutes
