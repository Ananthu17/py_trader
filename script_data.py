class StockData:
    def __init__(self):
        self.data = {
            'JSWSTEEL': 11723,
            'NTPC': 11630,
            'VEDL': 3063,
            'HINDALCO': 1363,
            'BPCL': 526,
            'TATASTEEL': 3499,
            'CIPLA': 694,
            'ITC': 1660,
            'WIPRO': 3787,
            'HDFCLIFE': 467,
            'BHARTIARTL': 10604,
            'ZOMATO': 5097,
            'BANKNIFTY': 999920005,
            'NIFTY': 999920000
        }

    def __getattr__(self, item):
        return self.data.get(item)


# Create an instance of the StockData class
script = StockData()
