from binance.client import Client

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret, testnet=True)

        # Explicitly set Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
