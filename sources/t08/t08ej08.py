from functools import wraps

def debug(func):
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

@debug
def add(x, y):
    """
        Función que suma dos números
    """
    return x + y
@debug
def sub(x, y):
    return x - y
@debug
def mul(x, y):
    return x * y
@debug
def div(x, y):
    return x / y

add(2, 2)
sub(8, 3)
mul(5,6)
div(16, 2)

help(add)