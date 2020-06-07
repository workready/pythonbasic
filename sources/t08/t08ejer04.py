class ClaseGenerica:
    pass # Tu codigo aqui


# Codigo de pruebas
c = ClaseGenerica(foo='bar', x=3, y=4, z=5)

assert(c.foo == "bar")
assert(c.x == 3)
assert(c.y == 4)
assert(c.z == 5)      
print(c)            # Salida esperada: ClaseGenerica: x=3,y=4,z=5,foo=bar. La lista de miembros no tiene porque ir en ese orden