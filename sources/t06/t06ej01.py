# Esta clase tiene atributos estáticos y dinámicos
class MiClase:
    # Estos atributos serían compartidos por todas las instancias de la clase
    x = 1
    y = 2

c = MiClase()
print(c.x, c.y) # 1, 2

# Nuevo atributo
c.z = 3
print(c.z)  # 3