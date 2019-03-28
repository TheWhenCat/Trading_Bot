import requests
import os
import matplotlib.pyplot as plt
import pandas
from io import StringIO
from functools import wraps
import inspect

'''
This wrapper has been based largely off of the RomelTorres/alpha_vantage wrapper(MIT License)
Taken core functions to re-fit them for my functions at the bottom
'''
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
            raise ValueError("No key supplied, please supply one\n"
                             "Or must be in a string format")

        self.key = key
        self.output_format = output_format

    @classmethod
    def output(cls, func):

        argspec = inspect.getfullargspec(func)

        try:
            positional_count = len(argspec.args) - len(argspec.defaults)
            defaults = dict(zip(argspec.args[positional_count:], argspec.defaults))
        except TypeError:
            if argspec.args:
                positional_count = argspec.args
                defaults = {}
            elif argspec.defaults:
                positional_count = 0
                defaults = argspec.defaults

        @wraps(func)
        def formatter(self, *args, **kwargs):

            used_kwargs = kwargs.copy()
            used_kwargs.update(zip(argspec.args[positional_count:], args[positional_count]))

            function_name, data_key, meta_data_key = func(self, *args, **kwargs)
            url = "{}function={}".format(request_builder.ALPHA_VANTAGE_API_URL, function_name)

            for idx, arg_name in enumerate(argspec.args[1:]):
                try:
                    arg_value = args[idx]
                except IndexError:
                    arg_value = used_kwargs[arg_name]
                if arg_value:
                    if isinstance(arg_value, tuple) or isinstance(arg_value, list):
                        arg_value = ','.join(arg_value)
                    url = '{}&{}={}'.format(url, arg_name, arg_value)
                if self._append_type:
                    url = '{}&apikey={}&datatype={}'.format(url, self.key, 'csv')
                if arg_value:
                    if isinstance(arg_value, tuple) or isinstance(arg_value, list):
                        arg_value = ','.join(arg_value)
                        url = '{}&{}={}'.format(url, arg_name, arg_value)
                return self.api_caller(url), data_key, meta_data_key
        return formatter

    def api_caller(self, url):

        response = requests.get(url)
        try:
            response = 200
        except:
            raise ConnectionError("A connection error is present,"
                                  "Status Code: {0}".format(response.status_code))
        response = StringIO(response.text)
        data = pandas.read_csv(response)
        return data


@request_builder
def Stock_Time_Series(self, params, *args, **kwargs):
    pass

@request_builder
def Foreign_Exchange(self, params, *args, **kwargs):
    pass

@request_builder
def Digital_Crypto_Currency(self, params, *args, **kwargs):
    pass

@request_builder
def Technical_Indicators(self, params, *arg, **kwargs):
    pass

r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=KE1NVXP9LYFO1Y5W&datatype=csv")
raw = StringIO(r.text)

data = pandas.read_csv(raw)
print(data)

plt.plot(data['close'], label="Experiment")

plt.show()

