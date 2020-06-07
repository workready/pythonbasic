# Creamos un descriptor
class Descriptor:
  # No nos hace falta get solo devolvería el valor
  def __init__(self, name=None):
    self.name = name
  def __set__(self, instance, value):
    instance.__dict__[self.name] = value

  # No dejamos borrar ningún campo
  def __delete__(self, instance):
    raise AttributeError("Can't delete")

# Clases para la comprobación de tipos
class Typed(Descriptor):
    ty = object
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected {}'.format(self.ty))
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class String(Typed):
    ty = str

class MayorDeEdad(Descriptor):
    def __set__(self, instance, value):
        if value < 18:
            raise ValueError('Expected >= 18')
        super().__set__(instance, value)

# Como hay herencia múltiple...
class IntegerMayorDeEdad(Integer, MayorDeEdad):
    pass

#Y lo aplicamos a nuestra clase
class Persona:
    def __init__(self, name, edad=18):
        self.name = name
        self.edad = edad

    name = String('name')
    edad = IntegerMayorDeEdad('edad')

# Ahora llamamos a nuestra clase
p = Persona('Paco')
p.edad = 21
p.name = 'Jorge'

print(p.edad)
print(p.name)

# Solo permitimos un entero y mayor de edad
p.edad = 12