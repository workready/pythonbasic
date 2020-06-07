una_lista = [1, 2, 3.0, 4 + 0j, "5"]
una_tupla = (1, 2, 3.0, 4 + 0j, "5")

print(una_lista[0])  # Primer elemento, 1
print(una_tupla[1])  # Segundo elemento, 2
print(una_lista[0:2])  # Desde el primero hasta el tercero, excluyendo este: 1, 2
print(una_tupla[:3])  # Desde el primero hasta el cuarto, excluyendo este: 1, 2, 3.0
print(una_lista[-1])  # El último: 4 + 0j
print(una_tupla[:])  # Desde el primero hasta el último
print(una_lista[::2])  # Desde el primero hasta el último, saltando 2: 1, 3.0