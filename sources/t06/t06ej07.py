# Aquí haremos algunas validaciones dentro de nuestros métodos get/set
class Person:
    def __init__(self, name, edad=18):
        # Aquí estamos llamando a los setters
        self.name = name
        self.edad = edad

    @property
    def name(self):
        return "{} es una bestia sexy".format(self._name) if self._name == "Jorge" else self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value > 17:
            self._edad = value
        else:
            raise ValueError("No puedes entrar a la discoteca, eres menor de edad")


p = Person('Paco')
print(p.name)

p.name = 'Jorge'
print(p.name)

p.edad = 15