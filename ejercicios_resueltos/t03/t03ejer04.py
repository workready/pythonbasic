def sumatorio(n):
    """
    Suma los n primeros números.
    Ejemplos
    --------
    >>> sumatorio(4)
    10
    """
    s = 0
    for x in range(1, n + 1):
        s = s + x
        
    return s

assert(sumatorio(4) == 10)