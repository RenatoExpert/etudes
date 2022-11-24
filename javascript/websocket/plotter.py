import json, sys

fpath = sys.argv[2] || 'dataframe.json'
file = open(fpath, 'r')
raw_string = file.read()
dataframe = json.loads(raw_string) 

import matplotlib.pyplot as plt
import numpy as np

b_ask_keys = list(dataframe['binance']['ask'].keys())
b_ask_x = np.array([int(x) for x in b_ask_keys])
b_ask_y = [float(dataframe['binance']['ask'][time]) for time in b_ask_keys]

o_bid_keys = list(dataframe['okx']['bid'].keys())
o_bid_x = np.array([int(x) for x in o_bid_keys])
o_bid_y = [float(dataframe['okx']['bid'][time]) for time in o_bid_keys]

print('Okx frames:' , len(o_bid_x))
print('Binance frames:' , len(b_ask_x))

fig, ax = plt.subplots(sharex=True, sharey=True)
ax.grid(True)

ax.plot(b_ask_x, b_ask_y, linewidth=0.5, color='red')
ax2 = ax.twinx()
ax2.plot(o_bid_x, o_bid_y, linewidth=0.5, color='blue')

ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_title('Binance asks versus Okx bids')
plt.show()

