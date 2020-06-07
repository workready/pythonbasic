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

# Decorando los métodos de una clase
def debugmethods(cls):
    for name, val in vars(cls).items():
        if callable(val):
            setattr(cls, name, debug(val)) # Aqui estamos aplicando el decorador debug anterior
    return cls

# Decorador para los atributos de una clase
def debugattr(cls):
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print('Get:', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__

    return cls

# Decorando la clase con dos decoradores a la vez
@debugattr
@debugmethods
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Punto(2, 3) # Punto.__init__

print(p.x)  # Get: x
print(p.y)  # Get: y