import functools

def debugargs(prefix=''):
    '''
    Un decorador que acepta argumentos
    '''
    def debug(func):
        '''
        El decorador en si
        '''
        msg = prefix + func.__qualname__
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return debug


@debugargs(prefix="------")
def add(x, y):
    return x + y
@debugargs(prefix="------")
def sub(x, y):
    return x - y
@debugargs(prefix="------")
def mul(x, y):
    return x * y
@debugargs(prefix="------")
def div(x, y):
    return x / y


add(2, 2)   # ------add
sub(8, 3)   # ------sub
mul(5,6)    # ------mul
div(16, 2)  # ------div