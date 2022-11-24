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
b_dict = dataframe['binance']
b_keys = list(b_dict.keys())
b_x = [int(x) for x in b_keys]
b_ya = [float(b_dict[time]['ask']) for time in b_keys]
b_yb = [float(b_dict[time]['bid']) for time in b_keys]
b_spreads =  [
	float(b_dict[time]['ask']) -
	float(b_dict[time]['bid'])
	for time in b_keys
]
b_as = get_average(b_spreads)

# ======= Okx ===========
o_dict = dataframe['okx']
o_dict = {int(k):v for k,v in o_dict.items()}
o_keys = list(o_dict.keys())
o_x = [int(x) for x in o_keys]
o_ya = [float(o_dict[time]['ask']) for time in o_keys]
o_yb = [float(o_dict[time]['bid']) for time in o_keys]
o_spreads =  [
	float(o_dict[time]['ask']) -
	float(o_dict[time]['bid'])
	for time in o_keys
]
o_as = get_average(o_spreads)

def force_y (dic, x):
	counter = 0
	while(true):
		i = x - counter
		if dic.has_key(i): return dic[i]
		else: counter+=1
	
def delta_range (a, b, 0):
	if a > 0 : return a
	elif b > 0 : return b
	else: return 0

# ======== Delta range ==
master_x = list(set(o_x)-set(b_x))
master_y = [
	delta_range(
		per_diff(force_y(o_dict, x), force_y(b_dict, x)),
		per_diff(force_y(b_dict, x),force_y(o_dict, x))
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

