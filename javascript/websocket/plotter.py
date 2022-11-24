import json, sys

fpath = sys.argv[1] or 'dataframe.json'
file = open(fpath, 'r')
raw_string = file.read()
dataframe = json.loads(raw_string) 

import matplotlib.pyplot as plt
import numpy as np

# ======= Binance =======
b_keys = list(dataframe['binance']['ask'].keys())
b_x = np.array([int(x) for x in b_keys])
b_ya = [float(dataframe['binance']['ask'][time]) for time in b_keys]
b_yb = [float(dataframe['binance']['bid'][time]) for time in b_keys]

# ======= Okx ===========
o_keys = list(dataframe['okx']['bid'].keys())
o_x = np.array([int(x) for x in o_keys])
o_ya = [float(dataframe['okx']['ask'][time]) for time in o_keys]
o_yb = [float(dataframe['okx']['bid'][time]) for time in o_keys]

# ===== Relatory ========
print('Okx frames:' , len(o_x))
print('Binance frames:' , len(b_x))


fig, axs = plt.subplots(4, 1, sharex=True, sharey=True)

# === Binance asks versus Okx bids ====
axs[0].set_title('Binance asks versus Okx bids')
axs[0].grid(True)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Price')
axs[0].plot(b_x, b_ya, linewidth=0.5, color='red')
ax02 = axs[0].twinx()
ax02.plot(o_x, o_yb, linewidth=0.5, color='blue')

# === Binance asks versus Okx bids ====
axs[1].set_title('Binance bids versus Okx asks')
axs[1].grid(True)
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Price')
axs[1].plot(o_x, o_ya, linewidth=0.5, color='red')
ax12 = axs[1].twinx()
ax12.plot(b_x, b_yb, linewidth=0.5, color='blue')

# === Okx spread ===
axs[2].set_title('Okx Spread')
axs[2].grid(True)
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Price')
axs[2].fill_between(o_x, o_ya, o_yb, linewidth=0.5, color='red')
#ax22 = axs[2].twinx()
#ax22.plot(b_x, b_yb, linewidth=0.5, color='gray')

# === Binance spread ===
axs[3].set_title('Binance Spread')
axs[3].grid(True)
axs[3].set_xlabel('Time')
axs[3].set_ylabel('Price')
axs[3].fill_between(b_x, b_ya, b_yb, linewidth=0.5, color='yellow')
#ax22 = axs[3].twinx()
#ax22.plot(b_x, b_yb, linewidth=0.5, color='blue')

fig.tight_layout()
plt.show()

