# Creamos una clase padre y una clase hija, que heredará sus métodos y atributos
class ClasePadre:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {0}, y={1}".format(self.x, self.y)

class OtraClasePadre:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def foo(self):
        return "foo"

# Entre paréntesis van las clases padres, separadas por comas
class ClaseHija(ClasePadre, OtraClasePadre):
    def __init__(self, x, y, z):

        # Podemos llamar al constructor del padre mediante super.
        # En caso de ambigüedad, como ahora, se llama al primero
        # de la lista (ClasePadre.__init__)
        super().__init__(x, y)

        # Y asignar nuestras propias variables
        self.z = z

    def __str__(self):
        # Podemos llamar a cualquier método de nuestra clase padre, igual que llamamos a __init__
        return "{0}, z={1}".format(super().__str__(), self.z)


padre = ClasePadre(3, 4)
hija = ClaseHija(5, 6, 7)

print(padre)    # x = 3, y=4
print(hija)     # x = 5, y=6, z=7
print(hija.foo())
