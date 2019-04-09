import requests
import os
import matplotlib.pyplot as plt
import pandas
from io import StringIO
from functools import wraps
import inspect
import warnings

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

    def __init__(self, key=None, output_format='pandas', url=ALPHA_VANTAGE_API_URL, *args, **kwargs):

        if key is None:
            key = os.getenv('ALPHAVANTAGE_API_KEY')
        if not key or not isinstance(key, str):
            raise ValueError("No key supplied, please supply one\n"
                             "Or must be in a string format")

        self.key = key
        self.output_format = output_format
        self.url = url

    @classmethod
    def output(cls, func):

        argspec = inspect.getfullargspec(func)
        print("Argspec: ", argspec)

        try:
            print("Route 1")
            positional_count = len(argspec.args) - len(argspec.defaults)
            defaults = dict(zip(argspec.args[positional_count:], argspec.defaults))
            print("Defaults: ", defaults)

        except TypeError:
            print("Route 2")
            if argspec.args:
                print(argspec.args)
                positional_count = argspec.args
                defaults = {}
            elif argspec.defaults:
                positional_count = 0
                defaults = argspec.defaults

        for key in defaults:
            if defaults[key] == None:
                warnings.warn("The {} key was deleted due to its value being {}".format(key, defaults[key]))

        @wraps(func)
        def formatter(self, *args, **kwargs):
            iter = 0
            for key in defaults:
                if iter == 0:
                    self.url = "{}{}={}".format(self.url, key, defaults[key])
                    iter +=1
                else:
                    self.url = "{}&{}={}".format(self.url, key, defaults[key])
                    iter += 1

            for idx, arg_name in enumerate(args):
                print(idx, arg_name)
                defaults[idx] = arg_name


            self.url = "{}&apikey={}&datatype={}".format(self.url, self.key, 'csv')
            print(self.url)

            return self.api_caller(self.url)
        return formatter

    def api_caller(self, url):

        response = requests.get(url)

        try:
            response == 200
        except:
            raise ConnectionError("A connection error is present,"
                                  "Status Code: {0}".format(response.status_code))
        print(response.text)
        response = StringIO(response.text)
        data = pandas.read_csv(response)
        print(data)
        return data

class Stock_Time_Series(request_builder):

    @request_builder.output
    def url_checker(self, function = "TIME_SERIES_INTRADAY", symbol = 'MSFT', interval = None, *args, **kwargs):
        pass

test = Stock_Time_Series(key = apikey)
x = test.url_checker("test", symbol='GOOGL', function='N/A', datatype="csv")

# @request_builder
# class Foreign_Exchange(apikey):
#     print(apikey)
#     pass
#
# @request_builder
# def Digital_Crypto_Currency(self, params, key = apikey, *args, **kwargs):
#     pass
#
# @request_builder
# def Technical_Indicators(self, params, key = apikey, *arg, **kwargs):
#     pass