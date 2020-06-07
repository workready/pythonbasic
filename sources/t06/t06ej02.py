# Podemos llamar a los métodos de la clase
class MiClase:
    x = 1
    y = 2

    def saludar(self):
        print("Hola")


c = MiClase()
c.saludar()

print(c.x, c.y)

# También podemos asignar el método a una variable y llamarlo después. Ojo: usamos el nombre del método sin paréntesis
saludo = c.saludar

# Ahora lo llamamos
saludo()