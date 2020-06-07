# Genera combinaciones de elementos de un iterable, cogidas de 2 en 2
import itertools
bases = "ATCG"

comb = itertools.combinations(bases, 2)
for c in comb:
    print(c, end=' - ')