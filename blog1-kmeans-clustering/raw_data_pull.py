
# coding: utf-8



from stocker.stocker import Stocker
import quandl
import yaml

import pandas as pd
import numpy as np
import datetime 
from dateutil.relativedelta import relativedelta




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
#         [['ticker', 'date', 'adj. open', 'adj. close', 'adj. volume']]     
    )
    return stock_history_df




first = True
for tick in ticker_list:
    if first:
        agg_df = agg_stock_data(tick)
        if agg_df.date.min().year <= 2003 and agg_df.date.max().year == 2018:
            first = False
    else:
        df = agg_stock_data(tick)
        if df.date.min().year <= 2003 and df.date.max().year == 2018:
            agg_df = pd.concat([agg_df, df], axis=0)




agg_df.head()




agg_df.to_csv('./agg_data2.csv')

