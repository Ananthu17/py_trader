class Info:
    def __init__(self, client):
        self.client = client

    def get_market_status(self):
        return [{data["ExchDescription"]: data["MarketStatus"]}
                for data in self.client.get_market_status()]
