import numpy as np

def Theta(x):
    """
    Implementación escalar de la función escalón de Heaviside
    https://es.wikipedia.org/wiki/Funci%C3%B3n_escal%C3%B3n_de_Heaviside
    """
    if x >= 0:
        return 1
    else:
        return 0


Theta(np.array([-3,-2,-1,0,1,2,3])) # Error!