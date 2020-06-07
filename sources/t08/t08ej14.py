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

#Y lo aplicamos a nuestra clase
class Persona:
    def __init__(self, name, edad=18):
        self.name = name
        self.edad = edad

    name = Descriptor('name')
    edad = Descriptor('edad')

# Ahora llamamos a nuestra clase
p = Persona('Paco')
p.edad = 21
p.name = 'Jorge'

print(p.edad)   # 21
print(p.name)   # Jorge

del(p.name)     # Esto provocará un error