import numpy as np
import random
import matplotlib.pyplot as plt
import inspect
# import scikit
import tensorflow



from AlphaVantage_Wrapper.API_Request import request_builder


apikey = 'KE1NVXP9LYFO1Y5W'

class Parser(request_builder):

    @request_builder.output
    def api_call(self, function, symbol, interval, *args, **kwargs):
        return data

    def plotter(self, data):

        parsed_time = {}
        for idx, time in enumerate(data['timestamp']):
                date, hour = time.split(' ')
                parsed_time[idx] = hour
        # print(parsed_time)
        for row in data:
            if row == 'timestamp':
                pass
            else:
                data_dict = {}
                for idx, value in enumerate(data[row]):
                    data_dict[idx] = value

                for idx in data_dict:
                    plt.plot(parsed_time[idx], data_dict[idx])
                    plt.show()


test = Parser(key = apikey)
data = test.api_call(symbol='GOOGL', function='TIME_SERIES_INTRADAY', interval='30min', datatype="csv")
test.plotter(data)