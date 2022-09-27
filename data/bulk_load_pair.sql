LOAD DATA
    LOCAL
    INFILE '/Users/fjaviersanchez/Repos/xTrader/data/XBTUSD_1.csv'
    IGNORE
    INTO TABLE xtrader_historical.historical_ohlc
    FIELDS
        TERMINATED BY ','
        ENCLOSED BY '"'
    LINES
        TERMINATED BY '\n'
    (datetime, open, high, low, close, volume, trades)
    SET frequency = 1;