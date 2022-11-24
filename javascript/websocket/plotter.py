import json, sys

fpath = sys.argv[1] or 'dataframe.json'
file = open(fpath, 'r')
raw_string = file.read()
dataframe = json.loads(raw_string) 

import matplotlib.pyplot as plt
import numpy as np

def get_average (list): 
	total = 0
	count = len(list)
	for n in list:
		total = total+n
	return total/count

# ======= Binance =======
b_keys = list(dataframe['binance'].keys())
b_x = [int(x) for x in b_keys]
b_ya = [float(dataframe['binance'][time]['ask']) for time in b_keys]
b_yb = [float(dataframe['binance'][time]['bid']) for time in b_keys]
b_spreads =  [
	float(dataframe['binance'][time]['ask']) -
	float(dataframe['binance'][time]['bid'])
	for time in b_keys
]
b_as = get_average(b_spreads)

# ======= Okx ===========
o_keys = list(dataframe['okx'].keys())
o_dict = dataframe['okx']
o_x = [int(x) for x in o_keys]
o_ya = [float(dataframe['okx'][time]['ask']) for time in o_keys]
o_yb = [float(dataframe['okx'][time]['bid']) for time in o_keys]
o_spreads =  [
	float(dataframe['okx'][time]['ask']) -
	float(dataframe['okx'][time]['bid'])
	for time in o_keys
]
o_as = get_average(o_spreads)

# ======== Delta range ==
'''
master_x = list(set(o_x)-set(b_x))
master_y = [
	choose(
		per_diff(force_y(),force_y()),
		per_diff(force_y(),force_y())
	)
	for x in master_x
]
'''

# ===== Relatory ========
print('Frames')
print('Okx:' , len(o_x))
print('Binance' , len(b_x))
print('Average Spread')
print('Okx:' , o_as)
print('Binance:' , b_as)

# === Ploting ======
fig, axs = plt.subplots(1, 1, sharex=True, sharey=False)
axs.set_title('Spreads')
axs.grid(True)
axs.set_xlabel('Time')
axs.set_ylabel('Price')

# === Okx spread ===
axs.fill_between(o_x, o_ya, o_yb, color='gray')
# === Binance spread ===
axs1 = axs.twinx()
axs1.fill_between(b_x, b_ya, b_yb, color='yellow')

fig.tight_layout()
plt.show()

