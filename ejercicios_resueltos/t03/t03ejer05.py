def sumatorio_tope(tope):
    """
    Va sumando números naturales hasta llegar al tope.
    
    Ejemplos
    --------
    >>> sumatorio_tope(9)
    6
    # 1 + 2 + 3
    
    >>> sumatorio_tope(10)
    10 # 1 + 2 + 3 + 4
    
    >>> sumatorio_tope(12)
    10 # 1 + 2 + 3 + 4
    
    
    >>> sumatorio_tope(16)
    15 # 1 + 2 + 3 + 4 + 5
    """
    s = 0
    n = 1
    while s + n <= tope:
        s += n
        n += 1
        
    return s

assert(sumatorio_tope(9) == 6)
assert(sumatorio_tope(10) == 10)
assert(sumatorio_tope(12) == 10)
assert(sumatorio_tope(16) == 15)