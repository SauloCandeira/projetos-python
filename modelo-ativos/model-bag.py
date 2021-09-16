import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

yf.pdr_override()
tickers = ["ABEV3.SA","ITSA4.SA", "VALE3.SA", "WEGE3.SA"] 
carteira = web.get_data_yahoo(tickers, period= "5y")["Close"]
ibov = web.get_data_yahoo("^BVSP", period= "5y")["Close"]










# ------------- MATPLOTLIB
#carteira_normalizada = (carteira / carteira.iloc[0])* 1000
#sns.set()
#carteira.plot(subplots=True, figsize=(22,8))
#carteira.plot(figsize=(22,8))
#carteira_normalizada.plot(figsize=(22,8))
#print(carteira)
#print(ibov)
#plt.legend()
#plt.show()

# ------------- PLOTLY
# Add data
#fig = go.Figure()

# Create and style traces
#fig.add_trace(go.Scatter(x=tickers, y=carteira, name='High 2014', 
#                         line=dict(color='firebrick', width=4)))
#fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
#                         line=dict(color='royalblue', width=4)))
#fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
#                         line=dict(color='firebrick', width=4,
#                              dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
#))
#fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
#                         line = dict(color='royalblue', width=4, dash='dash')))
#fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
#                         line = dict(color='firebrick', width=4, dash='dot')))
#fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
#                         line=dict(color='royalblue', width=4, dash='dot')))

# Edit the layout
#fig.update_layout(title='Average High and Low Temperatures in New York',
#                   xaxis_title='Month',
#                   yaxis_title='Temperature (degrees F)')

#fig = go.Figure(carteira.plot)
#carteira = go.Figure(subplots=True, figsize=(22,8))
#fig.show()
#plot(carteira)