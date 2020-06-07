import numpy as np
C = np.matrix([[1j, 2j], [3j, 4j]])

# Inversa
np.linalg.inv(C)
"""
    matrix([[ 0.+2.j ,  0.-1.j ],
        [ 0.-1.5j,  0.+0.5j]])
"""

# Comprobemos...
C.I * C
"""
matrix([[  1.00000000e+00+0.j,   4.44089210e-16+0.j],
        [  0.00000000e+00+0.j,   1.00000000e+00+0.j]])
"""

# Determinante
np.linalg.det(C)    # (2.0000000000000004+0j)

np.linalg.det(C.I)  # (0.50000000000000011+0j)