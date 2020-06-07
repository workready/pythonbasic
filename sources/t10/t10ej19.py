import numpy as np
C = np.matrix([[1j, 2j], [3j, 4j]])
C
"""
    matrix([[ 0.+1.j,  0.+2.j],
        [ 0.+3.j,  0.+4.j]])
"""

# Matriz conjugada
np.conjugate(C)
"""
matrix([[ 0.-1.j,  0.-2.j],
        [ 0.-3.j,  0.-4.j]])
"""

# Transpuesta + conjugada: conjugado hermitiano
C.H
"""
    matrix([[ 0.-1.j,  0.-3.j],
        [ 0.-2.j,  0.-4.j]])
"""

# Equivalente a arg de Matlab
np.angle(C+1)
"""
    array([[ 0.78539816,  1.10714872],
       [ 1.24904577,  1.32581766]])
"""