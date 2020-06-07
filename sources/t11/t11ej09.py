import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x ** 2 - y ** 2

x = np.linspace(-2, 2)
y = np.linspace(-2, 2)
xx, yy = np.meshgrid(x, y)
zz = f(xx, yy)

plt.contourf(xx, yy, zz, np.linspace(-4, 4, 100))
plt.colorbar()
plt.show()