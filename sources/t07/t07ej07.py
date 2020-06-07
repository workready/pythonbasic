# Ejemplo de ordenación de números aleatorios
import random

# Genera 10 números aleatorios entre 0 y 10000
rand_list = random.sample(range(10000), 10)

# Imprimimos la lista, la lista ordenada de menor a mayor, y de mayor a menor
print(rand_list)
print(sorted(rand_list))
print(sorted(rand_list, reverse=False))