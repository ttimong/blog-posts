
# coding: utf-8



from stocker.stocker import Stocker
import quandl
import yaml

import pandas as pd
import numpy as np
import datetime 
from dateutil.relativedelta import relativedelta


# # Using Stocker package to get data before 2018



with open("./api_key.yaml", 'r') as stream:
    try:
        data_loaded = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)




api_key = data_loaded['api_key']
quandl.ApiConfig.api_key = api_key




tickers = pd.read_csv('./tickers.csv')




ticker_list = [i for i in tickers.ticker]




def agg_stock_data(ticker):
    stock_object = Stocker(ticker)
    stock_history_df = stock_object.stock
    stock_history_df.columns = [i.lower() for i in stock_history_df.columns]
    stock_history_df = (
        stock_history_df
        .pipe(lambda x: x.assign(ticker=ticker))
    )
    return stock_history_df




first = True
for tick in ticker_list:
    if first:
        agg_df = agg_stock_data(tick)
        if agg_df.date.min().year <= 2006 and agg_df.date.max().year == 2018:
            first = False
    else:
        df = agg_stock_data(tick)
        if df.date.min().year <= 2006 and df.date.max().year == 2018:
            agg_df = pd.concat([agg_df, df], axis=0)




agg_df.head()




agg_df.to_csv('./2012_2017_data.csv')


# # Using Yahoo Finance Package



from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

yf.pdr_override()




first = True
for tick in ticker_list:
    try:
        start_2018_df = yf.download(tick, start="2018-01-03", end="2018-01-03").reset_index(drop=True)
        start_2018_df = (
            start_2018_df
            .pipe(lambda x: x.assign(date=datetime.date(2018, 1, 3)))
            .pipe(lambda x: x.assign(ticker='{}'.format(tick)))
        )
        end_2018_df = yf.download(tick, start="2018-12-29", end="2018-12-29").reset_index(drop=True)
        end_2018_df = (
            end_2018_df
            .pipe(lambda x: x.assign(date=datetime.date(2018, 12, 29)))
            .pipe(lambda x: x.assign(ticker='{}'.format(tick)))
        )
    except:
        ValueError
    if first is True:
        df_2018 = pd.concat([start_2018_df, end_2018_df], join='outer', axis=0)
        first = False
    else:
        intermediate_df = pd.concat([start_2018_df, end_2018_df], join='outer', axis=0)
        df_2018 = pd.concat([df_2018, intermediate_df], join='outer', axis=0)




df_2018.head(3)




df_2018.to_csv('./2018_data.csv')

