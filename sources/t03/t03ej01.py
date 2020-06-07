# Ejemplo sencillo de formateo de cadenas con variables posicionales
nombre = 'Jorge'
cualidad = 'sexy'

print("{0} es tremendamente {1}".format(nombre, cualidad))

# Puedo sustituir posiciones de un array
si_suffixes = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

print("1000{0[0]} = 1{0[1]}".format(si_suffixes)) # 1000KB = 1MB