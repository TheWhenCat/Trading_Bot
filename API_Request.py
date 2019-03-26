import requests
import time
from pprint import pprint
import matplotlib.pyplot as plt
import pandas

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

ts = TimeSeries(key='KE1NVXP9LYFO1Y5W', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['2. high'].plot()
plt.title("1 min Time Series High")
plt.show()

ti = TechIndicators(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='GOOGL', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  Google stock (60 min)')
plt.show()