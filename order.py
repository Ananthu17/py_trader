class Order:
    def __init__(self, client):
        self.client = client

    def place_order(self, OrderType, Exchange, ExchangeType, ScripCode,
                    Qty, Price, IsIntraday=False, IsStopLossOrder=False,
                    StopLossPrice=0, AHPlaced="N"):
        """
        Place an order in the market.

        Parameters:
        - OrderType (str): 'B' for BUY, 'S' for SELL.
        - Exchange (str): 'N' for NSE, 'B' for BSE, 'M' for MCX.
        - ExchangeType (str): 'C' for CASH, 'D' for DERIVATIVE, 'U' for CURRENCY.
        - ScripCode (int): The unique identifier for the scrip.
        - Qty (int): The quantity of shares or contracts to be traded.
        - Price (float): The price at which the order needs to be placed. Use 0 for MARKET orders.
        - IsIntraday (bool): Set to True for intraday orders, False for normal orders.
        - IsStopLossOrder (bool): Set to True if this order is a stop-loss order, False otherwise.
        - StopLossPrice (float): The stop-loss price for stop-loss orders. Default is 0.
        - AHPlaced (str): 'Y' if the order is placed after market hours, 'N' otherwise.

        Returns:
        - dict: A dictionary containing the order response.
        """
        order_data = {
            'OrderType': OrderType,
            'Exchange': Exchange,
            'ExchangeType': ExchangeType,
            'ScripCode': ScripCode,
            'Qty': Qty,
            'Price': Price,
            'IsIntraday': IsIntraday,
            'IsStopLossOrder': IsStopLossOrder,
            'StopLossPrice': StopLossPrice,
            'AHPlaced': AHPlaced
        }

        return self.client.place_order(**order_data)

    def bo_order(self, OrderType, Exchange, ExchangeType, ScripCode, Qty,
                 LimitPrice, TargetPrice, StopLossPrice, LimitPriceForSL,
                 TrailingSL, IsIntraday=True):
        """
        Place a bracket order in the market.

        Parameters:
        - OrderType (str): 'B' for BUY, 'S' for SELL.
        - Exchange (str): 'N' for NSE, 'B' for BSE, 'M' for MCX.
        - ExchangeType (str): 'C' for CASH, 'D' for DERIVATIVE, 'U' for CURRENCY.
        - ScripCode (int): The unique identifier for the scrip.
        - Qty (int): The quantity of shares or contracts to be traded.
        - LimitPrice (float): The limit price at which the main order needs to be placed.
        - TargetPrice (float): The target price for the bracket order.
        - StopLossPrice (float): The stop-loss trigger price for the bracket order.
        - LimitPriceForSL (float): The limit price at which the stop-loss order should be placed.
        - TrailingSL (float): The trailing stop-loss value (e.g., 0.5 for 0.5% trailing stop).
        - IsIntraday (bool): Set to True for intraday orders, False for normal orders.

        Returns:
        - dict: A dictionary containing the bracket order response.
        """
        bo_data = {
            'OrderType': OrderType,
            'Exchange': Exchange,
            'ExchangeType': ExchangeType,
            'ScripCode': ScripCode,
            'Qty': Qty,
            'LimitPrice': LimitPrice,
            'TargetPrice': TargetPrice,
            'StopLossPrice': StopLossPrice,
            'LimitPriceForSL': LimitPriceForSL,
            'TrailingSL': TrailingSL,
            'IsIntraday': IsIntraday,
        }

        return self.client.bo_order(**bo_data)

    def modify_order(self, ExchOrderID, Qty, Price):
        """
        Modify an existing order.

        Parameters:
        - ExchOrderID (str): The exchange order ID of the order to be modified.
        - Qty (int): The modified quantity of shares or contracts.
        - Price (float): The modified price of the order.

        Returns:
        - dict: A dictionary containing the modified order response.
        """
        return self.client.modify_order(ExchOrderID=ExchOrderID, Qty=Qty,
                                        Price=Price)

    def cancel_order(self, ExchOrderID):
        """
        Cancel an existing order.

        Parameters:
        - ExchOrderID (str): The exchange order ID of the order to be canceled.

        Returns:
        - dict: A dictionary containing the cancel order response.
        """
        return self.client.cancel_order(exch_order_id=ExchOrderID)

# Usage:
# Assuming you have a 'client' object already created, you can use
# the Order class like this:


# order = Order(client)

# Buy 1 share of scrip code 11915 at market price (intraday)
# print(order.place_order(OrderType='B', Exchange='N', ExchangeType='C',
#                         ScripCode=11915, Qty=1, Price=0, IsIntraday=True))

# Sell 1 share of scrip code 11915 at market price (intraday)
# print(order.place_order(OrderType='S', Exchange='N', ExchangeType='C',
#                         ScripCode=11915, Qty=1, Price=0, IsIntraday=True))

# Buy 1 share of scrip code 11915 at a limit price of 16.60
# print(order.place_order(OrderType='B', Exchange='N', ExchangeType='C',
#                         ScripCode=11915, Qty=1, Price=16.60))

# Sell 1 share of scrip code 11915 at a limit price of 16.65
# print(order.place_order(OrderType='S', Exchange='N', ExchangeType='C',
#                         ScripCode=11915, Qty=1, Price=16.65))

# Buy 1 share of scrip code 1660 at a limit price of 350 (intraday)
# print(order.place_order(OrderType='B', Exchange='N', ExchangeType='C',
#                         ScripCode=1660, Qty=1, Price=350, IsIntraday=True))

# Buy 1 share of scrip code 11915 at a limit price of 16.6 and place a stop-loss order at 16.5 (intraday)
# print(order.place_order(OrderType='B', Exchange='N', ExchangeType='C',
#                         ScripCode=11915, Qty=1, Price=16.6, IsIntraday=True,
#                         IsStopLossOrder=True, StopLossPrice=16.5))

# Place an offline order after market hours for scrip code 1660 at a limit price of 325
# print(order.place_order(OrderType='B', Exchange='N', ExchangeType='C',
#                         ScripCode=1660, Qty=1, Price=325, AHPlaced="Y"))

# Modify an existing order with ExchOrderID "1100000017861430" to have Qty=2 and Price=261
# print(order.modify_order(ExchOrderID="1100000017861430", Qty=2, Price=261))

# Cancel an existing order with ExchOrderID "1300000017992488"
# print(order.cancel_order(ExchOrderID="1300000017992488"))
