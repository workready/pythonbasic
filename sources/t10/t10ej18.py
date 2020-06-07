import numpy as np

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
np.dot(A, A)
"""
array([[ 300,  310,  320,  330,  340],
       [1300, 1360, 1420, 1480, 1540],
       [2300, 2410, 2520, 2630, 2740],
       [3300, 3460, 3620, 3780, 3940],
       [4300, 4510, 4720, 4930, 5140]])
"""

v1 = np.arange(0, 5)
np.dot(A, v1)   # array([ 30, 130, 230, 330, 430])
np.dot(v1, v1)  # 30

# También podemos hacer casting al tipo matrix. Eso cambia el comportamiento de los operadores +, -, * para usar álgebra matricial
M = np.matrix(A)
v = np.matrix(v1).T # vector columna
v
"""
matrix([[0],
        [1],
        [2],
        [3],
        [4]])
"""
M * M
"""matrix([[ 300,  310,  320,  330,  340],
        [1300, 1360, 1420, 1480, 1540],
        [2300, 2410, 2520, 2630, 2740],
        [3300, 3460, 3620, 3780, 3940],
        [4300, 4510, 4720, 4930, 5140]])
"""

M * v
"""
matrix([[ 30],
        [130],
        [230],
        [330],
        [430]])
"""

v.T * v # matrix([[30]])

v + M*v
"""
matrix([[ 30],
    [131],
    [232],
    [333],
    [434]])
"""

# Si intentamos operar entre elementos con dimensiones no compatibles, nos da error
v = np.matrix([1,2,3,4,5,6]).T
v
"""
matrix([[1],
        [2],
        [3],
        [4],
        [5],
        [6]])

"""

M * v   # Error: ValueError: shapes (5,5) and (6,1) not aligned: 5 (dim 1) != 6 (dim 0)