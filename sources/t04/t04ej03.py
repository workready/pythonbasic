# Implementación del mismo context manager usando contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        # La función se ejecuta hasta que encuentra una llamada a yield, y eso es lo que se devuelve en f
        yield f

    # Esto es lo último que se ejecuta en el context manager
    finally:
        f.close()

with custom_open('file.txt') as f:
    contents = f.read()
    print(contents)