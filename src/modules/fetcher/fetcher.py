import datetime
import logging
import time

import sources
import config
from kinesis.producer import KinesisProducer


class Fetcher:
    def __init__(self, source: sources.Source, pair: str, start_date: float, interval_secs: int) -> None:
        self._source = source
        self._ohlc = None
        if start_date < time.time():
            self.start_date = start_date
        else:
            raise ValueError(f'{start_date} is not a valid start date')
        if interval_secs > 0:
            self.interval_secs = interval_secs
        else:
            raise ValueError(f'{interval_secs} is not a valid interval')
        if pair in config.valid_pairs:
            self.pair = pair
        else:
            raise ValueError(f'{pair} is not a valid pair')

    @property
    def source(self) -> sources.Source:
        return self._source

    @source.setter
    def source(self, source: sources.Source) -> None:
        self._source = source

    @property
    def ohlc(self) -> sources.OHLC:
        return self._ohlc

    @ohlc.setter
    def ohlc(self, ohlc: sources.OHLC) -> None:
        self._ohlc = ohlc

    def fetch_next_ohlc(self):
        self.source.fetch_ohlc()

    def broadcast_ohlc(self):
        producer = KinesisProducer(stream_name='pyTrader')
        producer.put(self.ohlc, partition_key='incoming_ohlc')  #TODO: extract to config file

    def run(self) -> None:
        try:
            self.fetch_next_ohlc()
        except Exception as e:
            logging.error(f'failed to fetch ohlc: {e}')
        else:
            logging.info(f'fetched ohlc {self.ohlc}')
            try:
                self.broadcast_ohlc()
            except Exception as e2:
                logging.error(f'failed to broadcast ohlc: {e}')
            else:
                logging.info(f'broadcasted {self.ohlc}')
        while True:
            try:
                self.fetch_next_ohlc()
            except Exception as e:
                logging.error(f'failed to fetch ohlc: {e}')
            else:
                logging.info('fetched ohlc')
                time.sleep(self.interval_secs)
                try:
                    self.broadcast_ohlc()
                except Exception as e2:
                    logging.error(f'failed to broadcast ohlc: {e}')
                else:
                    logging.info(f'broadcasted {self.ohlc}')
