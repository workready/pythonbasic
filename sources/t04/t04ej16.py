# Generador a partir de una *generation expression*
numeros = (x*x for x in range(3))
for n in numeros:
    print(n, end=' ')

print()

# Si lo intentamos recorrer una segunda vez, esta vacio
for n in numeros:
    print(n, end=' ')
else:
    print("Generador vacío, tienes que volverlo a generar")