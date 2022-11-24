import json

file = open('dataframe.json', 'r')
raw_string = file.read()
dataframe = json.loads(raw_string) 

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

b_ask_x = dataframe['binance']['ask'].keys()
b_ask_y = [dataframe['binance']['ask'][time] for time in b_ask_x]

fig, ax = plt.subplots()
ax.plot(b_ask_x, b_ask_y, linewidth=0.5)
plt.show()

