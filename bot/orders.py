from .validators import validate_inputs

def place_order(
    client,
    logger,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):
    validate_inputs(symbol, side, order_type, quantity, price)
    client.client.futures_ping()
    client.set_leverage(symbol=symbol, leverage=1)

    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "positionSide": "BOTH"
    }

    if order_type == "LIMIT":
        order_data["price"] = price
        order_data["timeInForce"] = "GTC"

    logger.info(f"Order Request: {order_data}")

    try:
        response = client.place_order(**order_data)
        logger.info(f"Order Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
