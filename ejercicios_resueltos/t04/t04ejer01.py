class rango:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

# Esto va a llamar a nuestro iterador
z = rango(3)

assert(next(z) == 0)
assert(next(z) == 1)
assert(next(z) == 2)

try:
    next(z)
except StopIteration:
    print('Ya no puedes seguir llamando al iterador')
