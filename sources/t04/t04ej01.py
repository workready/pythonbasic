# Abrimos un fichero y escribimos texto dentro. No es necesario que lo cerremos. Se encarga el context manager
with open('file.txt', 'w') as f:
    f.write('hola')