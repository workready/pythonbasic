# Creamos conjunto con un elemento, y vemos su tipo
a_set = {1}
print(type(a_set)) # set

# Podemos meter todos los elementos que queramos
a_set = {1, 2}
print(a_set)


# Se puede crear un set a partir de una lista, pero no recuerda el orden
a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)

print(a_set)    # {False, True, 'a', 'mpilgrim', 42, 'b'}
print(a_list)   # ['a', 'b', 'mpilgrim', True, False, 42]