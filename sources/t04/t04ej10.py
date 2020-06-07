# Genera el producto cartesiano de dos iterables definidos como string
import itertools

cartesiano = itertools.product('ABC', '123')
for c in cartesiano:
    print(c, end=' - ')