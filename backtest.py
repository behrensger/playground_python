from backtesting import Strategy
from backtesting.lib import crossover
from nn_backtest.backtestdata import BacktestData
import pandas as pd


from backtesting.test import SMA
# https://kernc.github.io/backtesting.py/doc/backtesting/
# howtos:
# https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/
# https://blog.quantinsti.com/stock-market-data-analysis-python/


class SmaCross(Strategy):
    lang_n1 = 25
    lang_n2 = 45
    kurz_n1 = 3
    kurz_n2 = 8
    profit = 1

    def init(self):
        typical = (self.data.Close + self.data.Open + self.data.High
                   + self.data.Low)/4
        self.l1 = self.I(SMA, typical, self.lang_n1)
        self.l2 = self.I(SMA, typical, self.lang_n2)
        self.k1 = self.I(SMA, typical, self.kurz_n1)
        self.k2 = self.I(SMA, typical, self.kurz_n2)

    def next(self):
        if (self.l1 > self.l2) and crossover(self.k1, self.k2):
            self.buy()
            self.orders.set_tp(self.data.Close[-1]*(1 + (self.profit/1000)))
            self.orders.set_sl(self.data.Close[-1]*0.99)

        elif (self.l1 < self.l2) and crossover(self.k2, self.k1):
            self.sell()
            self.orders.set_tp(self.data.Close[-1]*(1 - (self.profit/1000)))
            self.orders.set_sl(self.data.High[-1]*1.01)

        if self.position and self.position.is_long and (
                crossover(self.k1, self.k2)):
            self.position.close()

        elif self.position and self.position.is_short and (
                crossover(self.k2, self.k1)):
            self.position.close()

# bt = Backtest(data, SmaCross, cash=100000, commission=0.0002)
# result = bt.run()
# print(result)
# bt.plot()
# stats = bt.optimize(profit=range(1,100, 1),
#                    maximize='Equity Final [$]'
#                    constraint=lambda p: p.kurz_n1 < p.kurz_n2)
#                )
# print(stats)


pathname = '/Users/abehrens/Documents/python/kursdaten'
file_filter = '*EURUSD*.csv'
bd = BacktestData()
df = bd.read_files(pathname, file_filter, 'H', False)
print(df.count())
