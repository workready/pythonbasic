# Iterador a partir de una función generadora
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

f = fib()

# Recorremos nuestro iterador, llamando a next(). Dentro del for se llama automáticamente a iter(f)
print(0, end=' ')
for n in range(16):
    print(next(f), end=' ')