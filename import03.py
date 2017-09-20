import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

        print(tickers)

        return tickers

# save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):

    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2017, 9, 8)

    for ticker in tickers: #for ticker in tickers[:25]: - it will download only 25 first tickers
        codeticker = ticker.replace('.','-').strip()
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.get_data_yahoo(codeticker, start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()


# Hello Harrison, thanks for the video.
# Another way to get the table is to use pandas:
# 1) df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
# 2) df.columns = df.ix[0] 3) df.drop(df.index[0], inplace=True)﻿

# I think you will need to install html5lib to get pandas_html working.﻿
# REPLY
