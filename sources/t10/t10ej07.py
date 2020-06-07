import numpy as np

# linspace, genera números igualmente espaciados
print(np.linspace(0, 10, 21))

"""
La salida será

array([  0. ,   0.5,   1. ,   1.5,   2. ,   2.5,   3. ,   3.5,   4. ,
         4.5,   5. ,   5.5,   6. ,   6.5,   7. ,   7.5,   8. ,   8.5,
         9. ,   9.5,  10. ])

np.logspace hace lo mismo pero con escala logarítmica
"""

# mgrid genera una meshgrid de Matlab
x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

"""
La salida del comando anterior será

[[0 0 0 0 0]
 [1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]
[[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]

Meshgrid en Matlab: http://es.mathworks.com/help/matlab/ref/meshgrid.html?requestedDomain=www.mathworks.com
"""