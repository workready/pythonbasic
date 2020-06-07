# El método private parece privado, pero vemos que realmente no lo es...
class MiClase:
    def public(self):
        print("Hola, soy un método público")

    def __private(self):
        print("Soy un método privado y no me puedes llamar, mwahahahaha")

c = MiClase()
c.public()

# Esta llamada nos dará un AttributeError, diciendo que no existe el método 'private'...
#c.__private()

# Pero así funciona...
#
c._MiClase__private()