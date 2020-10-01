#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 01:02:18 2019

@author: abehrens
"""
import os
import fnmatch
import pandas as pd


class BacktestData:
    ohlc_dict = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'}
    df = None

    def __init__(self):
        self.df = None

    def read_file(self, filename, timeframe):
        print("Read <"+filename+">")
        data = pd.read_csv(filename, sep=';', header=1,
                           names=('Date', 'Open', 'High', 'Low', 'Close',
                                  'Volume'),
                           parse_dates=['Date'],
                           index_col='Date'
                           )
        return data.resample('H').apply(self.ohlc_dict)

    def read_files(self, pathname, file_filter, timeframe,
                   verify_integrity=True):
        print("Read Files <"+file_filter+"> from path <"+pathname+">")

        for file in os.listdir(pathname):
            if fnmatch.fnmatch(file, file_filter):
                filename = os.path.join(pathname, file)
                if self.df is None:
                    self.df = self.read_file(filename, timeframe)
                else:
                    self.df = self.df.append(self.read_file(filename,
                                                            timeframe),
                                             verify_integrity=verify_integrity)

        self.df.sort_index(ascending=True, inplace=True)
        return self.df
