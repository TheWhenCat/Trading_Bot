import numpy as np
import random
import matplotlib.pyplot as plt
import inspect


from AlphaVantage_Wrapper.API_Request import request_builder


apikey = 'KE1NVXP9LYFO1Y5W'

class Stock_Time_Series(request_builder):

    @request_builder.output
    def api_call(self, function, symbol, interval, *args, **kwargs):
        return data

test = Stock_Time_Series(key = apikey)
data = test.api_call(symbol='GOOGL', function='TIME_SERIES_INTRADAY', interval='30min', datatype="csv")

plt.plot(data["close"])
plt.show()