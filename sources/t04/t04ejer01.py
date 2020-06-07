class rango:
    # Tu codigo aqui
    pass

# Esto va a llamar a nuestro iterador
z = rango(3)

assert(next(z) == 0)
assert(next(z) == 1)
assert(next(z) == 2)

try:
    next(z)
except StopIteration:
    print('Ya no puedes seguir llamando al iterador')