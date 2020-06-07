import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x ** 2)

x = np.linspace(-1, 3, 100)

plt.plot(x, f(x), color='red', linestyle='', marker='o')
plt.plot(x, 1 - f(x), c='g', ls='--')
plt.show()