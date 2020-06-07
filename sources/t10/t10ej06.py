import numpy as np

print(np.zeros(100))

"""
La salida será:
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
"""

print(np.zeros([10,10]))

"""
La salida será
array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
"""

print(np.empty(10))

"""
La salida será un array con valores despreciablemente pequeños. Algo como

array([  2.42613900e-316,   0.00000000e+000,   6.92720928e-310,
         6.92720926e-310,   6.92722586e-310,   6.92720926e-310,
         0.00000000e+000,   0.00000000e+000,   6.92722899e-310,
         6.36598737e-311])

La creación de este array tarda menos que la creación del array de ceros. Pero tengamos en cuenta que, aunque pequeños, los valores usados para las celdas serán arbitrarios
"""

print(np.ones([3, 2]))

"""
La salida será

array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])

También pueden ser útiles las funciones np.zeros_like y np.ones_like. Se puede consultar lo que hacen con

help(np.zeros_like)
help(np.ones_like)
"""

# Array identidad
print(np.identity(4))

"""
La salida será

array([[ 1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.]])

Esta función es un caso particular de np.eye. Se puede consultar su ayuda con

help(np.eye)
"""

# Matriz diagonal
print(np.diag([1,2,3]))
"""
    La salida será
    [[1 0 0]
    [0 2 0]
    [0 0 3]]
"""

# Matriz diagonal con offset
print(np.diag([1,2,3], k=1))
"""
    La salida será
    [[0 1 0 0]
    [0 0 2 0]
    [0 0 0 3]
    [0 0 0 0]]
"""

# Matriz 5 x 5 con números aleatorios entre 0 y 1.
print(np.random.rand(5,5))

# Lo mismo pero siguiendo una distribución normal
print(np.random.randn(5,5))

# Array con elementos que van de 0 a 5
print(np.arange(0, 5)) # array([0, 1, 2, 3, 4])

# Array de 0 a 10, de 3 en 3
print(np.arange(0,11,3))   # array([0, 3, 6, 9])

