# Usando itertools.zip_longest para generar tuplas a partir de iterables de diferente longitud
import itertools

a = [1,2,3]
b = [9,10]

print([i for i in itertools.zip_longest(a, b)])