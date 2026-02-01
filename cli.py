import argparse
import os
from dotenv import load_dotenv

load_dotenv()
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    log_file = "logs/market_order.log" if args.type == "MARKET" else "logs/limit_order.log"
    logger = setup_logger(log_file)

    print("\n📤 Order Request Summary")
    print(vars(args))

    client = BinanceFuturesClient(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET")
    )

    try:
        response = place_order(
            client,
            logger,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Placed Successfully")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))

if __name__ == "__main__":
    main()
