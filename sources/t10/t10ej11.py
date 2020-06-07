import numpy as np

A = np.array([[1, 2], [3, 4]])
A
"""
    array([[1, 2],
           [3, 4]])
"""

# Esto sería un puntero: si cambiamos B, A también cambia
B = A

# Esto sería una copia: si cambiamos B, A no cambia
B = np.copy(A)