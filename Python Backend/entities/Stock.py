class Stock:
    def __init__(self, symbol, price, estimate, prices):
        self.symbol = symbol
        self.price = price
        self.estimate = estimate
        self.prices = prices

    def to_dict(self):
        return {'symbol': self.symbol, 'price': self.price, 'estimate': self.estimate,
                'prices': self.prices}
