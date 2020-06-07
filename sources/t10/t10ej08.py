import numpy as np

a = np.arange(1,10)
print(a)

M = np.reshape(a, [3,3])
print(M)
# Valdria también a.reshape([3, 3])

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
n,m = A.shape
print(A)

B = A.reshape((1, n*m))
print(B)


# Podemos también modificar directamente el array
B[0,0:5] = 5 # aqui estamos modificando el array. El original cambia también
print(B)
print(A)

# Podemos aplanar el array original
A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
B = A.flatten()
# Modifiquemos ahora un elemento de B. A no cambia porque flatten hace copia
B[0:5] = 10

print(A)
print(B)