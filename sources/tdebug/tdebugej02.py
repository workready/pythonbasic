import pdb

# Ahora la función no tiene puntos de parada
def debug_this(i1, i2):
    result = i1
    for i in range(5):
        result += i2
    return result

# Pero ya la llamo yo
pdb.runcall(debug_this, 10, 20)