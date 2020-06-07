import numpy as np
import os

data = np.genfromtxt(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'stockholm_td_adj.tsv'))

np.shape(data)  # (77431, 7)

# la temperatura está en la columna 3
np.mean(data[:,3])  # 6.1971096847515854


# Desviación estándar y varianza
np.std(data[:,3]), np.var(data[:,3])    # (8.2822716213405734, 68.596023209663414)

# máx y min

# Media diaria más baja
data[:,3].min() # -25.800000000000001

# Media diaria más alta
data[:,3].max() # 28.300000000000001