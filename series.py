import decimal
import pandas as pd
import time


class Series:
    def __init__(self, pair: str, interval: int, last: decimal.Decimal):
        self.pair = pair
        self.interval = interval
        self.last = last
        self.data = pd.DataFrame(columns=['time', 'o', 'h', 'l', 'c'])
