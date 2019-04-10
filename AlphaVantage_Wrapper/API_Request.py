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
            iter = 0
            for key in defaults:
                if defaults[key] ==None:
                    try:
                        defaults[key] = kwargs[key]
                    except:
                        raise KeyError("Please provide a value for the default specified")
                if iter == 0:
                    self.url = "{}{}={}".format(self.url, key, defaults[key])
                    iter +=1
                else:
                    self.url = "{}&{}={}".format(self.url, key, defaults[key])
                    iter += 1

            for idx, arg_name in enumerate(kwargs):
                try:
                    defaults[arg_name]
                except:
                    self.url = "{}&{}={}".format(self.url, arg_name, kwargs[arg_name])

            self.url = "{}&apikey={}".format(self.url, self.key)

            return self.api_caller(self.url)
        return formatter

    def api_caller(self, url):

        response = requests.get(url)

        try:
            response == 200
        except:
            raise ConnectionError("A connection error is present,"
                                  "Status Code: {0}".format(response.status_code))

        response = StringIO(response.text)
        data = pandas.read_csv(response)
        return data