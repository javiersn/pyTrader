# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import decimal
import time
import api
import fetcher
import series


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pair = 'XXBTZUSD'
    interval = 10

    print(f'{str(time.time())}\tconnecting to Kraken...')
    k = api.API()
    print(f'{str(time.time())}\tconnected')
    s = series.Series(pair, interval, decimal.Decimal(time.time()))
    print(f'{str(time.time())}\tfetching data for {pair} every {interval} seconds')
    f = fetcher.Fetcher(k, s)
    f.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
