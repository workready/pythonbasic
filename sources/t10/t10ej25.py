import numpy as np

def Theta(x):
    """
    Implementación "vector-aware" de la misma función
    """
    return 1 * (x >= 0)

Theta(np.array([-3,-2,-1,0,1,2,3]))

# array([0, 0, 0, 1, 1, 1, 1])

# También funciona para escalares
Theta(-1.2), Theta(2.6) # (0, 1)