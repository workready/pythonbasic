def printer():
    """
        Corrutina que simplemente recibe datos y los imprime por pantalla
    """
    print("Preparado para imprimir...")
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print("Cerrando printer")

# Esta es la función a implementar. Tiene que:
# 1. Recibir datos del programa (g.send)
# 2. Filtrar esos datos y mandárselos a la corrutina que imprime por pantalla (printer)
def grep(pattern, consumer):
    """
        Corrutina que filtra datos y se los manda a otra corrutina
    """
    print("Buscando la cadena {}".format(pattern))
    try:
        while True:
            s = (yield)
            if pattern in s:
                consumer.send(s)
    except GeneratorExit:
        print("Cerrando grep")
        consumer.close()


# Creamos la corrutina final y la arrancamos (las corrutinas se arrancan con send(None))
p = printer()
p.send(None)

# Creamos la corrutina que filtra y la arrancamos
g = grep("ending", p)
g.send(None)

# Este es el texto que metemos en nuestra cadena de corrutinas, de manera que:
# 1. La corrutina filtra las palabas
# 2. Le manda a la corrutina printer las palabras filtradas para que las imprima
text = 'Commending spending is offending to people pending lending!'

# Vamos mandando texto a la corrutina principal
for line in text.split():
    g.send(line)

#  Y cerramos
g.close()