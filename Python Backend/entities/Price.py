class Price:
    def __init__(self, open, close, high, low, volume):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume

    def to_dict(self):
        return {'open': self.open, 'close': self.close, 'high': self.high,
                'low': self.low, 'volume': self.volume}
