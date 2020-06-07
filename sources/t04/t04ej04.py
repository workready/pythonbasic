# Una lista es un iterable
a_list = [1, 2, 3]
for a in a_list:
    # Tip: para que print no meta un salto de línea al final de cada llamada, pasarle un segundo argumento end=' '
    print (a, end=' ')

# Un string también es un iterable
a_string = "hola"
for a in a_string:
    print(a, end=' ')