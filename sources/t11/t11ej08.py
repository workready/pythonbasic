import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x ** 2 - y ** 2

x = np.linspace(-2, 2)
y = np.linspace(-2, 2)
xx, yy = np.meshgrid(x, y)
zz = f(xx, yy)

plt.contour(xx, yy, zz)
plt.colorbar()
plt.show()