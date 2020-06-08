import numpy as np

b = np.zeros((3, 4))
b[-1] = np.arange(5, 9)
print(b)