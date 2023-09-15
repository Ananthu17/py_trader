max_loss = 3000


number_of_trades = 3

single_trade_loss = max_loss / number_of_trades


def planner(stock_price, capital):

    capital = capital//2
    leverage = 5
    quantity = capital*leverage//stock_price
    stop_loss = round(single_trade_loss/quantity, 1)
    return {"Quantity": quantity, "StopLoss": stop_loss, "Target": stop_loss*2}



print(planner(168.8, 3000))


class TradePlanner:

    def __init__(self, capital, max_risk_in_a_day, reward)
        self.capital = capital
        self.max_risk_in_a_day = risk_percentage