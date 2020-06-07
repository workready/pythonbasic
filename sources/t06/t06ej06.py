class Person:
    def __init__(self, name):
        # En esta asignación, realmente estamos llamando al setter de más abajo
        self.name = name

    @property   # <1>
    def name(self):
        return self._name

    @name.setter    # <2>
    def name(self, value):
        self._name = value

    # Mediante el decorator @name.deleter, permitiremos eliminar una propiedad de nuestra persona
    @name.deleter
    def name(self):
        del self._name

p = Person('Paco')
print(p.name)

p.name = 'Jorge'
print(p.name)

del p.name
print(p.name)   # Esto provoca una excepcion, porque el campo ya no existe