# Implementamos un constructor para nuestra clase, y dentro del constructor asignamos variables.
class MiClase:
    def __init__(self, x, y):

        # self.x y self.y son propias de la instancia, no compartidas
        self.x = x
        self.y = y

c = MiClase(7, 12)

print(c.x, c.y)