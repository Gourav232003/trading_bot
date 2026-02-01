from binance.client import Client
import os

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def set_leverage(self, symbol: str, leverage: int = 1):
        return self.client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )
    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)
