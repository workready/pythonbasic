import numpy as np

B = np.array([2 ** i for i in range(36)]).reshape((6,6))
print(B)

print(np.linalg.det(B))