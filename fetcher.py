import time

import api
from series import *

time_idx = 0
open_idx = 1
high_idx = 2
low_idx = 3
close_idx = 4


class Fetcher:
    def __init__(self, kraken_api: api.API, series: Series):
        self.api = kraken_api
        self.series = series

    def fetch_new(self):
        # request data to public api
        res = self.api.fetch_ohlc(self.series.pair, self.series.last)
        # validate response
        if 'error' not in res:
            print(f'{decimal.Decimal(time.time())}\tmissing "error" object in response\t{res}')
            return
        if len(res['error']) > 0:
            print(f'{decimal.Decimal(time.time())}\tignoring response with non-empty error\t{res}')
            return
        if 'result' not in res:
            print(f'{decimal.Decimal(time.time())}\tmissing "result" object in response\t{res}')
            return
        if self.series.pair not in res['result']:
            print(f"{decimal.Decimal(time.time())}\tmissing pair '{self.series.pair}' data in response\t{res}")
            return
        # process results
        print(f"{decimal.Decimal(time.time())}\tprocesing response with {len(res['result'][self.series.pair])} results\t{res}")
        for r in res['result'][self.series.pair]:
            print(f"{decimal.Decimal(time.time())}\tfetched '{r}'")
            if r[time_idx] > self.series.last:
                self.series.last = r[time_idx]
                # TODO: current candle's closing price is not reliable until the next candle appears
                continue
            if r[time_idx] > self.series.last:
                pass
                # TODO: overwrite current row with the response's data
        return

    def run(self):
        while True:
            time.sleep(self.series.interval)
            self.fetch_new()

