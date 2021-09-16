import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
import pyfolio as pf
import warnings 

warnings.filterwarnings('ignore')
yf.pdr_override()


tickers = ["XRP-USD","BTC-USD", "ETH-USD", "TRX-USD"] #RIPPLE X BITCOIN
carteira = web.get_data_yahoo(tickers, start="2020-01-01")["Close"]
carteira.plot(subplots=True, figsize=(22,8))
print(carteira)
plt.legend()
plt.show()






