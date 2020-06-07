# MiClase tendrá un constructor alternativo, que usará una lista en lugar de una cadena
class Persona:
    def __init__(self, nombre=''):
        self.nombre = nombre

    @classmethod
    def fromList(cls, l):

        # Instanciamos un nuevo objeto de la clase
        x = cls()

        # Lo rellenamos y lo devolvemos
        x.nombre = ' '.join([l[0], l[1]])
        return x

    def __str__(self):
        return self.nombre


p = Persona("Pepito Perez")
p2 = Persona.fromList(["Jorge", "Blanco"])

print(p)    # Pepito Perez
print(p2)   # Jorge Blanco