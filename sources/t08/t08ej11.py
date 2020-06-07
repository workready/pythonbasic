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

@debugmethods
class MiClase:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self):
        pass

    def bar(self):
        pass


c = MiClase(2, 3)   # MiClase.__init__
c.foo() # MiClase.foo
c.bar() # MiClase.bar