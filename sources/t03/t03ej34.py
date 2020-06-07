# Definir función que multiplica dos números. Por defecto, el segundo de ellos valdrá 2
def multiplica(x, y=2.0):
    """Multiplica dos números, por defecto el primero por 2."""
    return x * y

assert(multiplica(2, 3) == 6)
assert(multiplica(4) == 8) # 8