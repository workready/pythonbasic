# Creando nuestra propia *generator function*
def generatorFunction(limit):
    for n in range(limit):
        yield n*n # <--- Yield again!

numeros = generatorFunction(3)
for n in numeros:
    print(n, end=' ')