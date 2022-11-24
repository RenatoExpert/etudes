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
b_dict = {
	int(k):{
		side: float(v[side])
		for side in v
	} for k,v in dataframe['binance'].items()
}
b_keys = list(b_dict.keys())
b_x = [int(x) for x in b_keys]
b_ya = [b_dict[time]['ask'] for time in b_keys]
b_yb = [b_dict[time]['bid'] for time in b_keys]
b_spreads =  [
	float(b_dict[time]['ask']) -
	float(b_dict[time]['bid'])
	for time in b_keys
]
b_as = get_average(b_spreads)

# ======= Okx ===========
o_dict = {
	int(k):{
		side: float(v[side])
		for side in v
	} for k,v in dataframe['okx'].items()
}
o_keys = list(o_dict.keys())
o_x = [int(x) for x in o_keys]
o_ya = [o_dict[time]['ask'] for time in o_keys]
o_yb = [o_dict[time]['bid'] for time in o_keys]
o_spreads =  [
	float(o_dict[time]['ask']) -
	float(o_dict[time]['bid'])
	for time in o_keys
]
o_as = get_average(o_spreads)

# ======== Delta range ==
def force_y (dic, x, side):
	counter = 0
	while(counter<100):
		i = x - counter
		if i in dic:
			return dic[i][side]
		else:
			counter+=1
	return None
	
def delta_range (a, b):
	if (a is None or b is None):
		return None
	elif (a>b):
		return a
	else:
		return b

def per_diff (a, b):
	if (a is None or b is None):
		return None
	else:
		diff = a-b
		if diff > 0:
			return 100*(diff/a)
		else:
			return 0

master_x = sorted(list(set(o_x)-set(b_x)))
master_y = [
	delta_range(
		per_diff(force_y(o_dict, x, 'bid'), force_y(b_dict, x, 'ask')),
		per_diff(force_y(b_dict, x, 'bid'), force_y(o_dict, x, 'ask'))
	)
	for x in master_x
]

# ===== Relatory ========
print('Frames')
print('Okx:' , len(o_x))
print('Binance' , len(b_x))
print('Average Spread')
print('Okx:' , o_as)
print('Binance:' , b_as)

# === Ploting ======
ax1 = plt.subplot(
	311, 
	xlabel='Time(ms)', 
	ylabel='Price(USDT)', 
	title='Spreads'
)
plt.grid(True)

# === Okx spread ===
plt.fill_between(o_x, o_ya, o_yb, color='gray')
# === Binance spread ===
plt.fill_between(b_x, b_ya, b_yb, color='yellow')
# === Delta range
axs3 = plt.subplot(
	312,
	sharex=ax1,
	title='Arbitrage delta',
	xlabel='Time(ms)',
	ylabel='Delta(%)'
)
plt.plot(master_x, master_y, color='green')

plt.tight_layout()
plt.show()

