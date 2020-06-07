# Genera todas las permutaciones de 4 elementos usando itertools
import itertools

elementos = [1, 2, 3, 4]
permutaciones = itertools.permutations(elementos)
for p in permutaciones:
    print(p, end=' - ')