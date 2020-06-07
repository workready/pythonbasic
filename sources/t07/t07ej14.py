# Usando itertools.cycle para generar tuplas a partir de iterables de diferente longitud
import itertools

A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]

zip_list = zip(A, itertools.cycle(B)) if len(A) > len(B) else zip(itertools.cycle(A), B)
print([z for z in zip_list])