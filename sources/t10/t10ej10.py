import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
"""
    a vale
    [[1 2]
    [3 4]]
"""

# repite cada elemento 3 veces
np.repeat(a, 3) # array([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])

# otro tipo de repetición
np.tile(a, 3)
"""
    array([[1, 2, 1, 2, 1, 2],
    [3, 4, 3, 4, 3, 4]])
"""

# Concatenación
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
"""
    array([[1, 2],
           [3, 4],
           [5, 6]])
"""

# Con .T tenemos la traspuesta de una matriz, como veremos luego
np.concatenate((a, b.T), axis=1)
"""
    array([[1, 2, 5],
           [3, 4, 6]])
"""

# vstack y hstack
np.vstack((a,b))
"""
    array([[1, 2],
           [3, 4],
           [5, 6]])
"""

np.hstack((a,b.T))
"""
array([[1, 2, 5],
       [3, 4, 6]])
"""