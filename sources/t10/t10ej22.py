import numpy as np
import os

data = np.genfromtxt(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'stockholm_td_adj.tsv'))

mask_feb = data[:,1] == 2

# La temperatura está en la columna 3
np.mean(data[mask_feb,3])   # -3.2121095707365961

# Podemos hasta graficarlo
import matplotlib.pyplot as plt

months = np.arange(1,13)
monthly_mean = [np.mean(data[data[:,1] == month, 3]) for month in months]

fig, ax = plt.subplots()
ax.bar(months, monthly_mean)
ax.set_xlabel("Month")
ax.set_ylabel("Monthly avg. temp.");

plt.show()