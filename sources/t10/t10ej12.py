import numpy as np

#crear un array y y sumarle un número
arr = np.arange(11)
arr + 55    # array([55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65])

#multiplicarlo por un número
arr * 2     # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20])

#elevarlo al cuadrado
arr ** 2    # array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])

#calcular una función
np.tanh(arr)

"""
La salida será

array([ 0.        ,  0.76159416,  0.96402758,  0.99505475,  0.9993293 ,
        0.9999092 ,  0.99998771,  0.99999834,  0.99999977,  0.99999997,  1.        ])

"""

#creamos dos arrays
arr1 = np.arange(0,11)
arr2 = np.arange(20,31)

#los sumamos
arr1 + arr2     # array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

#multiplicamos
arr1 * arr2     # array([  0,  21,  44,  69,  96, 125, 156, 189, 224, 261, 300])

# >,<
arr1 > arr2

"""
    La salida será

    array([False, False, False, False, False, False, False, False, False,
           False, False], dtype=bool)

"""
# ==
arr1 == arr2 # ¡ojo! los arrays son de integers, no de floats

"""
    La salida será

    array([False, False, False, False, False, False, False, False, False,
       False, False], dtype=bool)
"""

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
A * A # el termino en ingles es element-wise
"""
array([[   0,    1,    4,    9,   16],
       [ 100,  121,  144,  169,  196],
       [ 400,  441,  484,  529,  576],
       [ 900,  961, 1024, 1089, 1156],
       [1600, 1681, 1764, 1849, 1936]])
"""

v1 = np.arange(0, 5)    # [0 1 2 3 4]
v1 * v1                 # array([ 0,  1,  4,  9, 16])
