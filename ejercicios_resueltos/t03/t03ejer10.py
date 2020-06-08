def suma(*args):
    """
        Función que devuelve el sumatorio de todos sus argumentos
        @param *args: lista de números de longitud arbitraria
        @returns: Sumatorio de todos los argumentos
    """
    s = args[0]
    for a in args[1:]:
        s = s + a
    return s

assert(suma(1, 2, 3, 4, 5, 6, 7) == 28)