import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import yfinance as yf

yf.pdr_override()
tickers = ["XRP-USD","BTC-USD", "ETH-USD", "SOL1-USD"] #RIPPLE X BITCOIN
carteira = web.get_data_yahoo(tickers)["Close"]
#carteira = web.get_data_yahoo(tickers, start="2020-01-01")["Close"]
carteira.plot(subplots=True, figsize=(22,8))
print(carteira)
plt.legend()
plt.show()






