# mutable vs immutable
s = "hola" # s es un string. Es immutable
l = ["h", "o", "l", "a"] # l es una lista. Es mutable.

# ok, se puede cambiar el objeto sin cambiar la variable que lo apunta
l[0] = "b"

# error, no se puede cambiar el objeto sin cambiar la variable que lo apunta. Tendríamos que cambiar el objeto entero.
s[0] = "b"