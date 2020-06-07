# Construir iterador para generar secuencia de Fibonacci
import itertools

class Fib:
    '''Iterador que genera la secuencia de Fibonacci'''

    # Constructor
    def __init__(self):
        self.prev = 0
        self.curr = 1

    # Esto es llamado cada vez que se llama a iter(Fib). Algo que for hace automáticamente, pero lo podríamos hacer a mano.
    # La función __iter__ debe devolver cualquier objeto que implemente __next__. En este caso, la propia clase
    def __iter__(self):
        return self

    # Esto es llamado cada vez que se llama a next(Fib). Algo que for hace automáticamente, pero lo podríamos hacer a mano.
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

# f guarda un iterador. En este momento no se ha llamado a nada, solo se ha construido el iterador
f = Fib()

# Recorremos nuestro iterador, llamando a next(). Dentro del for se llama automáticamente a iter(f)
print(0, end=' ')
for n in range(16):
    print(next(f), end=' ')

# Otra manera más elegante de hacerlo, con itertools
#print([0] + list(itertools.islice(f, 0, 16)))