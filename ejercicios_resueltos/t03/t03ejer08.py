def fib(n):
    """
        Devuelve el término n de la secuencia de Fibonacci
        @param n: posición a devolver
        @return: El término n de la secuencia
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b  # Bendita asignación múltiple
    return a

def fib_recursivo(n):
    """
        Función recursiva que devuelve el término n de la secuencia de Fibonacci
        @param n: posición a devolver
        @return: El término n de la secuencia
    """
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib_recursivo(n - 1) + fib_recursivo(n - 2)
    return res

def n_primeros(n):
    """
        Devuelve los n primeros términos de la secuencia de Fibonacci
        @param n: Número de términos a devolver
        @return: Lista con los n primeros términos
    """
    F = fib_recursivo
    lista = []
    for ii in range(n):
        lista.append(F(ii))
    return lista

    # Esto es mas pythonista, lo veremos en el siguiente tema
    #return [fib_recursivo(ii) for ii in range(n)]


# Comprobaciones
assert(fib(5) == 5)
assert(fib_recursivo(0) == 0)
assert(fib_recursivo(3) == 2)
assert(fib(8) == 21)
assert(n_primeros(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])