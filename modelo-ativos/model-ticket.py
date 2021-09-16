import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf


yf.pdr_override()
#ibov = web.get_data_yahoo('^BVSP')
ibov = web.get_data_yahoo('BTC', start= '2020-10-01', end='2021-09-01')
print(ibov)
#ibov2008 = ibov[ibov.index.year == 2008]
Close = ibov['Close'].plot()
Media21 = ibov['Close'].rolling(21).mean().plot(label='MM21')
Media200 = ibov['Close'].rolling(200).mean().plot(label='MM200')
plt.legend()
plt.show()



