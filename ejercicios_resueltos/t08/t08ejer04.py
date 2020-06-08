class ClaseGenerica:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        attrs = ["{}={}".format(k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s: %s" % (classname, ",".join(attrs))


# Codigo de pruebas
c = ClaseGenerica(foo='bar', x=3, y=4, z=5)

assert(c.foo == "bar")
assert(c.x == 3)
assert(c.y == 4)
assert(c.z == 5)      
print(c)            # Salida esperada: ClaseGenerica: x=3,y=4,z=5,foo=bar. La lista de miembros no tiene porque ir en ese orden