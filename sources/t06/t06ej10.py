# Definimos un método de clase, que podemos llamar tanto desde la clase en si como desde una instancia de la misma
class MiClase:
    def f(self):
        print("Esto es un método de instancia")

    # Método de clase: no recibe la instancia self como parámetro
    @classmethod
    def classf(*_):
        print(*_)
        print("Esto es un método de clase")


c = MiClase()
c.f()

# Podemos llamar al método desde la clase o desde la instancia
c.classf(4,5,6,7,8,9)
MiClase.classf()

# No podríamos hacer esto
# MiClase.f()