class Stock:
    def __init__(self, symbol, price, estimate, earning, prices):
        self.symbol = symbol
        self.price = price
        self.estimate = estimate
        self.earning = earning
        self.prices = prices

    def to_dict(self):
        return {'symbol': self.symbol, 'price': self.price, 'estimate': self.estimate,
                'earning': self.earning, 'prices': self.prices}
