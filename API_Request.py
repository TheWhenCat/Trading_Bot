import requests
import os
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

    def __init__(self, key=None, output_format='pandas', *args, **kwargs):

        if key is None:
            key = os.getenv('ALPHAVANTAGE_API_KEY')
        if not key or not isinstance(key, str):
            raise ValueError("No key supplied, please supply one")

        self.key = key
        self.output_format = output_format

        





    def Stock_Time_Series(self):

    def Foreign_Exchange(self):

    def Digital_Crypto_Currency(self):

    def Technical_Indicators(self):



r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=KE1NVXP9LYFO1Y5W&datatype=csv")
raw = StringIO(r.text)

data = pandas.read_csv(raw)
print(data)

plt.plot(data['close'], label="Experiment")

plt.show()
