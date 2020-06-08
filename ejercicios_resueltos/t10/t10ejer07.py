import numpy as np

C =  np.array([[1,2,4],\
               [6,5,8],\
               [2,2,11]])

np.linalg.det(C)

C_inv = np.linalg.inv(C)
print(C_inv)

# Por verificar...
print(C_inv.dot(C))