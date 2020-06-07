import numpy as np

# Usando list comprehension para indexar

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
A

"""
    La salida será

    array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14],
       [20, 21, 22, 23, 24],
       [30, 31, 32, 33, 34],
       [40, 41, 42, 43, 44]])
"""

# Aplicando máscaras
B = np.array([n for n in range(5)])
print(B)    # [0 1 2 3 4]

row_mask = np.array([True, False, True, False, False])
print(B[row_mask])  # [0 2]

# Con máscaras podemos seleccionar condicionalmente elementos de un array
x = np.arange(0, 10, 0.5)
print(x)

"""
    La salida será

[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5  7.
  7.5  8.   8.5  9.   9.5]
"""

mask = (5 < x) * (x < 7.5)
print(mask)

"""
    La salida será

    [False False False False False False False False False False False  True
  True  True  True False False False False False]
"""