# Añadimos atributos a una instancia de una clase, una vez creada
class Empleado(object):
    "Clase para definir a un empleado"
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def getNombre(self):
        return self.nombre

# Nombre de la clase
print(Empleado.__name__)   # Empleado

jorge = Empleado("Jorge", "jorge@mail.com")
# Identificador de creador
assert(isinstance(jorge, Empleado) is True)

# Acceso a docstring
print(Empleado.__doc__) # Clase para definir a un empleado