import functools

def debug(func=None, prefix=''):
    '''
    Decorador que permite llamada tanto sin argumentos como con ellos
    '''
    if func is None:
        # Si la llamada se ha hecho sin método, es la llamada con atributos, de manera que devolvemos
        # una llamada al decorador, con un valor ya prefijado para prefix
        return functools.partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

@debug(prefix="++++++++")
def add(x, y):
    return x + y
@debug
def sub(x, y):
    return x - y
@debug(prefix="********")
def mul(x, y):
    return x * y
@debug
def div(x, y):
    return x / y


add(2, 2)   # ++++++++add
sub(8, 3)   # sub
mul(5,6)    # ********mul
div(16, 2)  # div