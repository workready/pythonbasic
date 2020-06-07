# Mal, esto no es pythonista
numeros = range(10)
multiplos_de_3 = list() # Otra manera de declarar una lista
for element in numeros:
    if not element % 3:
        multiplos_de_3.append(element)

print(multiplos_de_3)