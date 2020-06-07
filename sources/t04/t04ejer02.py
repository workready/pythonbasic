# Tu codigo aqui
def grango(n):
    pass

# Esto va a llamar a nuestro generador
z = grango(3)

assert(next(z) == 0)
assert(next(z) == 1)
assert(next(z) == 2)

try:
    next(z)
except StopIteration:
    print('Ya no puedes seguir llamando al generador')
