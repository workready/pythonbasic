import numpy as np
import matplotlib.pyplot as plt


tablero = np.zeros((8, 8))
tablero[1::2, ::2] = 1
tablero[::2, 1::2] = 1

plt.matshow(tablero, cmap=plt.cm.gray_r)

plt.show()