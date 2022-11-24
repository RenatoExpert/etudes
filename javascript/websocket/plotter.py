import json

file = open('dataframe.json', 'r')
raw_string = file.read()
dataframe = json.loads(raw_string) 

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

b_ask_keys = list(dataframe['binance']['ask'].keys())
b_ask_x = [int(x) for x in b_ask_keys]
b_ask_y = [dataframe['binance']['ask'][time] for time in b_ask_keys]

o_bid_keys = list(dataframe['okx']['bid'].keys())
o_bid_x = [int(x) for x in o_bid_keys]
o_bid_y = [dataframe['okx']['bid'][time] for time in o_bid_keys]

ref_x = b_ask_x + o_bid_x
ref_y = [0 for x in ref_x]

fig, ax = plt.subplots()
#ax.plot(b_ask_x, b_ask_y, o_bid_x, o_bid_y, linewidth=0.5)
ax.plot(ref_x, ref_y, linewidth=0.5, color='white')
ax.plot(b_ask_x, b_ask_y, linewidth=0.5, color='red')
ax.plot(o_bid_x, o_bid_y, linewidth=0.5, color='blue')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_title('Binance asks versus Okx bids')
#ax.grid(True)
plt.show()

