import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return np.log(x) - np.sin(x)

x = np.linspace(0, 10, num=100)
plt.plot(x, F(x), 'k', lw=2, label="$F(x)$")
plt.plot(x, np.log(x), label="$\log{x}$")
plt.plot(x, np.sin(x), label="$\sin{x}$")
plt.plot(x, np.zeros_like(x), 'k--')
plt.legend(loc=4)
plt.show()