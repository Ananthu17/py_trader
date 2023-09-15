from py5paisa import FivePaisaClient
from decouple import config
from info import Info
from order import Order
from book import Tradebook
from script_data import script
import json

# Load variables from the .env file
APP_NAME = config('APP_NAME')
APP_SOURCE = config('APP_SOURCE')
USER_ID = config('USER_ID')
PASSWORD = config('PASSWORD')
USER_KEY = config('USER_KEY')
ENCRYPTION_KEY = config('ENCRYPTION_KEY')

cred = {
    "APP_NAME": APP_NAME,
    "APP_SOURCE": APP_SOURCE,
    "USER_ID": USER_ID,
    "PASSWORD": PASSWORD,
    "USER_KEY": USER_KEY,
    "ENCRYPTION_KEY": ENCRYPTION_KEY
}

# Login
client = FivePaisaClient(email=config('EMAIL'), passwd=config('PASSWD'),
                         dob=config('DOB'), cred=cred)
client.login()

market_info = Info(client)
order = Order(client)
book = Tradebook(client)
print(book.get_positions())


req_list = [
            { "Exch": "N", "ExchType":"C", "ScripCode":11915},
        ]

req_data=client.Request_Feed('mf','s',req_list)
def on_message(ws, message):
    desired_keys = ['Exch', 'Token', 'LastRate', 'LastQty', 'LastQty']
    print([{key: entry[key] for key in desired_keys} for entry in json.loads(message)])


client.connect(req_data)

client.receive_data(on_message)


class TrailingStopLoss:
    def __init__(self, buy_price, stop_loss_percent=5, trail_percent=10):
        self.buy_price = buy_price
        self.stop_loss_percent = stop_loss_percent
        self.trail_percent = trail_percent
        self.current_stop_loss = buy_price * (1 - (stop_loss_percent / 100))
        self.price_increase_counter = 0

    def set_initial_stop_loss(self, stop_loss_percent):
        self.stop_loss_percent = stop_loss_percent
        self.current_stop_loss = self.buy_price * (1 - (stop_loss_percent / 100))

    def update_stop_loss(self, current_price):
        if current_price > self.buy_price:
            price_increase = ((current_price - self.buy_price) / self.buy_price) * 100
            if price_increase >= self.trail_percent:
                self.price_increase_counter += 1
                self.set_initial_stop_loss(
                    self.stop_loss_percent - (self.price_increase_counter * 5)
                )
        return self.current_stop_loss


# Example usage:
buy_price = 17.55
trade_data = [{'Exch': 'N', 'Token': 11915, 'LastRate': 17.55, 'LastQty': 15588}]
positions_open = {1: {'BuyQty': 1, 'BuyValue': 17.55, 'Exch': 'N', 'ScripCode': 11915, 'ScripName': 'YESBANK'}}

for trade in trade_data:
    scrip_code = trade['Token']
    if scrip_code in positions_open:
        position_info = positions_open[scrip_code]
        tsl = TrailingStopLoss(position_info['BuyValue'])
        current_price = trade['LastRate']
        new_stop_loss = tsl.update_stop_loss(current_price)
        print(f"Scrip Code: {scrip_code}, Current Price: {current_price}, New Stop Loss: {new_stop_loss}")
