import numpy as np

M = np.dot(
np.array([
    [2, 0, 0],
    [-1, 1, 0],
    [3, 2, -1]
]),
np.array([
    [1, 1, 1],
    [0, 1, 2],
    [0, 0, 1]
]))

x = np.linalg.solve(M, np.array([-1, 3, 0]))
print(x)
