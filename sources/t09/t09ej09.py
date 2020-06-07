def reader():
    """Simula leer de un socket, de un fichero, etc"""
    for i in range(4):
        yield i

def reader_wrapper(g):
    # Iteramos sobre el generador hijo, generando el valor que nos devuelva
    yield from g

wrap = reader_wrapper(reader())
for i in wrap:
    print(i)