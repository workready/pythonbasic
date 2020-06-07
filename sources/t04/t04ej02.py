class CustomOpen(object):
    # Constructor de la clase
    def __init__(self, filename):
      self.file = open(filename)

    # Esto es lo que se devuelve en el with, y va a la variable f
    def __enter__(self):
        return self.file

    # Esto se ejecuta antes de terminar el context manager
    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        print('adios')
        self.file.close()

with CustomOpen('file.txt') as f:
    contents = f.read()
    print(contents)