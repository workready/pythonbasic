# pop devuelve el último elemento extraído, y clear elimina todos los elementos
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
print(a_set)    # {1, 3, 6, 10, 15, 21, 28, 36, 45}

a_set.pop() # 1
a_set.pop() # 3

a_set.clear()
print(a_set)    # set()


# Discard y remove se diferencian en que, si el elemento no existe, remove lanza una excepcion y discard no
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
print(a_set)    # {1, 3, 36, 6, 10, 45, 15, 21, 28}

a_set.discard(10)
print(a_set)    # {1, 3, 36, 6, 45, 15, 21, 28}

a_set.discard(10)
print(a_set)    # {1, 3, 36, 6, 45, 15, 21, 28}

a_set.remove(21)
print(a_set)    # {1, 3, 36, 6, 45, 15, 28}

a_set.remove(21)    # Excepción