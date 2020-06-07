# Deconstruyendo nuestra función generadora...

def generatorFunction():
    # Ni siquiera necesitamos limite. Vamos a llamar a yield 3 veces, simulando lo que pasaría dentro del bucle
        yield 0
        yield 1
        yield 4

numeros = generatorFunction()

# En lugar de hacer un bucle, llamemos 3 veces seguidas a next(), que es lo que hace el for
print(next(numeros))
print(next(numeros))
print(next(numeros))

# Si intentamos acceder a un generador agotado, se lanza una excepción de tipo StopIteration
# La capturamos y terminamos silenciosamente, que es lo que hace for
try:
    print(next(numeros))
except StopIteration as e:
    pass # No hacemos nada