import requests
import time
from pprint import pprint
import matplotlib.pyplot as plt
import pandas
from io import StringIO

#request parameters
function = 'TIME_SERIES_INTRADAY'
symbol = 'GOOGL'
interval = '60min'
datatype = 'csv'
apikey = 'KE1NVXP9LYFO1Y5W'

class request_builder(object):

    ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query?"

    def __init__(self):
        request = ALPHA_VANTAGE_API_URL + 'function=' + function


r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=KE1NVXP9LYFO1Y5W&datatype=csv")
raw = StringIO(r.text)

data = pandas.read_csv(raw)
print(data)

plt.plot(data['close'], label="Experiment")

plt.show()
