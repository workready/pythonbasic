import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x ** 2)

x = np.linspace(-1, 3, 100)

with plt.style.context('ggplot'):
    plt.plot(x, f(x))
    plt.plot(x, 1 - f(x))

plt.show()