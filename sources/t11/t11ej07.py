import numpy as np
import matplotlib.pyplot as plt


N = 100
s = np.abs(50 + 50 * np.random.randn(N))
c = np.random.randn(N)

x = np.random.randn(N)
y = np.random.randn(N)

plt.scatter(x, y, s=s, c=c, cmap=plt.cm.Blues)
plt.colorbar()
plt.show()