import numpy as np
import random
import matplotlib.pyplot as plt
import inspect
import scikit-learn
import tensorflow



from AlphaVantage_Wrapper.API_Request import request_builder


apikey = 'KE1NVXP9LYFO1Y5W'

class Parser(request_builder):

    @request_builder.output
    def api_call(self, function, symbol, interval, *args, **kwargs):
        return data

    def plotter(self, data):


test = Parser(key = apikey)
data = test.api_call(symbol='GOOGL', function='TIME_SERIES_INTRADAY', interval='30min', datatype="csv")

plt.plot(data["close"])
plt.show()