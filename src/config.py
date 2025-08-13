TELEGRAM_TOKEN = "ISI_TOKEN_TELEGRAM"
TELEGRAM_CHAT_ID = "ISI_CHAT_ID"
BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# Setting proxy (Cloudflare 1.1.1.1 dan Google 8.8.8.8 tidak langsung dipakai di Python)
# Pakai proxy publik atau socks5 agar bisa lolos blokir
PROXIES = {
    "http": "socks5h://127.0.0.1:1080",
    "https": "socks5h://127.0.0.1:1080"
}
