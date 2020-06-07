
# Escribimos un decorador
def debug(func):

    # Ojo, que qualname vino en la 3.3: https://www.python.org/dev/peps/pep-3155/
    msg = func.__qualname__
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


# Aplicamos nuesto decorador a la función add
def add(x, y):
    """
        Función que suma dos números
    """
    return x + y

# Y llamamos a nuestra función add decorada
res = debug(add)(2,2)
print(res)