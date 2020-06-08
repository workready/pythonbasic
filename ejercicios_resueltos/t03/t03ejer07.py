import math

# Para Python inferior a 3.5, podemos usar esta función-
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def raiz(S):
    """
        Devuelve la raiz cuadrada de S calculada mediante el método babilónico
    """
    x = S / 2
    while True:
        temp = x
        x = (x + S / x) / 2

        # Doc de isclose: https://docs.python.org/3/library/math.html#math.isclose
        # Guia para precisión: https://en.wikipedia.org/wiki/Machine_epsilon#Values_for_standard_hardware_floating_point_arithmetics
        if math.isclose(temp, x):
            return x

S = 10
x = raiz(S)

# Puedes comparar x con math.sqrt(S). Es posible que el valor sea ligeramente diferente, debido a la precisión 
print(x)
print(math.sqrt(S))
