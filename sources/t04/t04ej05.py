# Construimos iterable (lista) a partir de una comprehension list
numeros = [x*x for x in range(3)]
for n in numeros:
    print(n, end=' ')