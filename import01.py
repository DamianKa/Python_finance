import bs4 as bs
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

save_sp500_tickers()



# Hello Harrison, thanks for the video.
# Another way to get the table is to use pandas:
# 1) df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
# 2) df.columns = df.ix[0] 3) df.drop(df.index[0], inplace=True)﻿

# I think you will need to install html5lib to get pandas_html working.﻿
# REPLY
