

class Tradebook:
    def __init__(self, client):
        self.client = client

    desired_keys = ['BuyQty', 'BuyValue', 'Exch', 'ScripCode', 'ScripName']

    # Fetches holdings
    def get_holdings(self):
        return self.client.holdings()

    # Fetches margin
    def get_margins(self):
        return self.client.margin()

    # Fetches positions
    def get_positions(self):
        return self.ordered_book(self.client.positions())
        # return self.client.positions()

    # Fetches the order book of the client
    def get_orderbook(self):
        return self.client.order_book()

    # Fetches Trade book
    def get_tradebook(self):
        return self.client.get_tradebook()

    # utils
    def ordered_book(self, book_type):
        cleaned_data = [{key: entry[key] for key in self.desired_keys} for entry in book_type]
        return [{index: item} for index, item in enumerate(cleaned_data, 1)]
