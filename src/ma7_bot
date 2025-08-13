import requests
import json
from datetime import datetime
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, BINANCE_URL, PROXIES

def get_binance_data():
    try:
        r = requests.get(BINANCE_URL, proxies=PROXIES, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        send_telegram(f"[MA7 BOT] ERROR: {e}")
        return None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print(f"Telegram Error: {e}")

if __name__ == "__main__":
    data = get_binance_data()
    if data:
        send_telegram(f"[MA7 BOT] Data OK: {datetime.now()}")
