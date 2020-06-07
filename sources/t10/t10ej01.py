import numpy as np

# Array de una dimensión
mi_primer_array = np.array([1, 2, 3, 4])
print(mi_primer_array)

# Comprobar el tipo de mi_primer_array
assert(type(mi_primer_array) == np.ndarray)   # numpy.ndarray

# Comprobar el tipo de datos que contiene
assert(mi_primer_array.dtype == np.dtype('int64'))   # dtype('int32') o dtype('int64')

# Si queremos cambiar el tipo de los elementos del array
otro_array = mi_primer_array.astype('int32')    # o int64, según
assert(otro_array.dtype == np.dtype('int32'))

# Queremos saber sus dimensiones
assert(mi_primer_array.shape == (4, ))   # (4, )

# Y el número de elementos que contiene
assert(mi_primer_array.size == 4)    # 4

# Array de dos dimensiones
mi_segundo_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mi_segundo_array)