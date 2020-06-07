# Una lista es un iterable
a_list = [1, 2, 3]

# Creamos dos iteradores a partir de la lista, mediante la función iter()
it1 = iter(a_list)
it2 = iter(a_list)

# Vamos recorriendo el iterador 1, consumiendo un elemento en cada paso, mediante la función next()
print(next(it1))
print(next(it1))

# Ahora recorremos el iterador 2, que seguirá en la primera posición
print(next(it2))