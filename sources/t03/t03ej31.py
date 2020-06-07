# Mal, esto no es pythonista
pares = [2, 4, 6, 8, 10, 12, 14]
hay_impar = False
for n in pares:
    if n % 2:
        hay_impar = True
        break

if not hay_impar:
    print('Todos los números son pares')


# Bien, esto es pythonista
pares = [2, 4, 6, 8, 10, 12, 14]
for n in pares:
    if n % 2:
        break

# El else se va a ejecutar después del bucle siempre y cuando no lo rompamos de manera abrupta con un break
else:
    print('Todos los números son pares')