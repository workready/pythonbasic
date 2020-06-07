# Añadimos atributos a una instancia de una clase, una vez creada
class Empleado(object):
    "Clase para definir a un empleado"
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def getNombre(self):
        return self.nombre


jorge = Empleado("Jorge", "jorge@mail.com")
jorge.guapo = "Por supuesto"

print("Es Jorge guapo: {}".format(jorge.guapo)) # Es Jorge guapo: Por supuesto