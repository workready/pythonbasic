# Añadimos elementos con add. Si añadimos un elemento que ya existe, no hace nada
a_set = {1, 2, 3}
print(a_set)    # {1, 2, 3}

a_set.add(4)
print(a_set)    # {1, 2, 3, 4}

a_set.add(1)
print(a_set)    # {1, 2, 3, 4}


# Con update, es como si llamaramos a add varias veces
a_set = {1, 2, 3}
print(a_set)    # {1, 2, 3}

a_set.update({4, 5, 6})
print(a_set)    # {1, 2, 3, 4, 5, 6}