import numpy as np
from numpy.linalg import det

A = np.array([
    [1, 0, 0],
    [2, 1, 1],
    [-1, 0, 1]
])
B = np.array([
    [2, 3, -1],
    [0, -2, 1],
    [0, 0, 3]
])

print(A)
print(B)

C = np.dot(A, B)
print(C)

print(det(C))