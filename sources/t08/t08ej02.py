class Empleado(object):
    "Clase para definir a un empleado"
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def getNombre(self):
        return self.nombre


jorge = Empleado("Jorge", "jorge@mail.com")
jorge.guapo = "Por supuesto"

# Probando hasattr, getattr, setattr
print(hasattr(jorge, 'guapo'))  # True
print(getattr(jorge, 'guapo'))  # Por supuesto

print(hasattr(jorge, 'listo'))  # False
setattr(jorge, 'listo', 'Más que las monas')
print(getattr(jorge, 'listo'))  # Mas que las monas