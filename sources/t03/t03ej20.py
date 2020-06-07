# Podemos construir un set a partir de una lista, y se eliminarán los duplicados directamente
a_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(a_list)   # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

a_set = set(a_list)
print(a_set)    # {1, 2, 3, 4}