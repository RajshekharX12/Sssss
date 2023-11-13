import time
import requests
from pyrogram import Client

# Your Telegram Bot Token
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Your Telegram Channel ID (replace with your channel ID)
CHANNEL_ID = -100123456789

# CoinCap API URL for Bitcoin
COINCAP_API_URL = "https://api.coincap.io/v2/assets/bitcoin"

# Function to get Bitcoin prices
def get_bitcoin_price():
    try:
        response = requests.get(COINCAP_API_URL)
        data = response.json()
        bitcoin_price = data["data"]["priceUsd"]
        return f"BTC ${bitcoin_price}"
    except Exception as e:
        print(f"Error getting Bitcoin price: {e}")
        return None

# Pyrogram client setup
app = Client(
    "bitcoin_price_bot",
    bot_token=BOT_TOKEN,
)

# Function to update channel description
def update_channel_description():
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price:
        try:
            app.set_chat_description(CHANNEL_ID, bitcoin_price)
            print(f"Channel description updated: {bitcoin_price}")
        except Exception as e:
            print(f"Error updating channel description: {e}")

# Main loop to update every 5 minutes
while True:
    update_channel_description()
    time.sleep(300)  # 5 minutes
