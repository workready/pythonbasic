# Ejemplo de función filter
def es_impar(x):
    return x % 2

print(list(filter(es_impar, range(10))))