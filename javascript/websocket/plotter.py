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
b_x = np.array([int(x) for x in b_keys])
b_ya = [float(dataframe['binance'][time]['ask']) for time in b_keys]
b_yb = [float(dataframe['binance'][time]['bid']) for time in b_keys]

# ======= Okx ===========
o_keys = list(dataframe['okx'].keys())
o_x = np.array([int(x) for x in o_keys])
o_ya = [float(dataframe['okx'][time]['ask']) for time in o_keys]
o_yb = [float(dataframe['okx'][time]['bid']) for time in o_keys]
o_spreads =  [
	float(dataframe['okx'][time]['bid']) -
	float(dataframe['okx'][time]['ask']) 
	for time in o_keys
]
o_as = get_average(o_spreads)

# ===== Relatory ========
print('Frames')
print('Okx:' , len(o_x))
print('Binance' , len(b_x))
print('Average Spread')
print('Okx:' , o_spreads)



fig, axs = plt.subplots(1, 1, sharex=True, sharey=False)

# === Okx spread ===
axs.set_title('Spreads')
axs.grid(True)
axs.set_xlabel('Time')
axs.set_ylabel('Price')
axs.fill_between(o_x, o_ya, o_yb, color='gray')

# === Binance spread ===
axs1 = axs.twinx()
axs1.fill_between(b_x, b_ya, b_yb, color='yellow')

fig.tight_layout()
plt.show()

