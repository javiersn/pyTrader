CREATE DATABASE xtrader_historical;

create table xtrader_historical.historical_ohlc
(
    datetime  bigint unsigned   not null,
    pair      char(8)           not null,
    frequency smallint unsigned not null,
    open      decimal(10, 4)    null,
    high      decimal(10, 4)    null,
    low       decimal(10, 4)    null,
    close     decimal(10, 4)    null,
    trades    int unsigned      null,
    volume    decimal(13, 8)    null,
    primary key (datetime, pair, frequency)
);

create index i_datetime
    on xtrader_historical.historical_ohlc (datetime);

create index i_pair_frequency
    on xtrader_historical.historical_ohlc (pair, frequency);

grant delete, drop, insert, select, update on table xtrader_historical.historical_ohlc to 'admin';
