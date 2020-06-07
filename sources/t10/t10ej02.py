import numpy as np

# Array de una dimensión
mi_primer_array = np.array([1, 2, 3, 4])

# Suma
assert(np.sum(mi_primer_array) == 10) # 10

# Máximo
assert(np.max(mi_primer_array) == 4) # 4

# Seno
print(np.sin(mi_primer_array))

# Constantes
print(np.pi, np.e)