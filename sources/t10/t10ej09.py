import numpy as np

v = np.array([1,2,3])
print("Vector")
print(v)    # [1 2 3]

np.shape(v) # (3,)

# Creamos matriz columna
v[:, np.newaxis]
"""
    v valdrá:
    array([[1],
       [2],
       [3]])
"""

v[:,np.newaxis].shape   # (3, 1)

# Matriz fila
v[np.newaxis,:].shape   # (1, 3)