import decimal
import random
import time
from abc import ABC, abstractmethod
from typing import Type

import config


class OHLC:
    def __init__(self, pair: str, timestamp: float, o: float, h: float, l: float, c: float, vol: float):
        self.pair = pair
        self.timestamp = timestamp
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.vol = vol

    def __repr__(self):
        return f'{{"pair":"{self.pair}", "timestamp":"{self.timestamp}", "o":"{self.o}", "h":"{self.h}", "l":"{self.l}", "c":"{self.c}", "vol":"{self.vol}"}}'


class Source(ABC):
    @abstractmethod
    def fetch_ohlc(self, pair: str, start_time: float) -> OHLC:
        pass


class GeneratorSource(Source):
    PRICE_MEAN = 20000
    PRICE_VARIANCE = 100
    STEP_VARIANCE = 20
    VOL_MEAN = 200000
    VOL_VARIANCE = 100000
    SIM_ITERS = 20

    def fetch_ohlc(self, pair: str, start_time: float) -> OHLC:
        sim = []
        for i in range(GeneratorSource.SIM_ITERS):
            if i == 0:
                pm = GeneratorSource.PRICE_MEAN
            else:
                pm = random.normalvariate(sim[i-1], GeneratorSource.PRICE_VARIANCE)
            sim.append(random.normalvariate(pm, GeneratorSource.PRICE_VARIANCE))
        vol = random.normalvariate(GeneratorSource.VOL_MEAN, GeneratorSource.VOL_VARIANCE)
        return OHLC(pair, start_time, [0], max(sim), min(sim), sim[19], vol)

    @property
    def __class__(self: _T) -> Type[_T]:
        return super().__class__()
