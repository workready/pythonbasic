# Implementamos un método __unicode__ que será llamado cuando pasemos una instancia de la clase como argumento de print()
class MiClase:
    def __init__(self, x, y):

        # self.x y self.y son propias de la instancia, no compartidas
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {0}, y={1}".format(self.x, self.y)

c = MiClase(7, 12)
print(c)    # x=7, y=12