import time
from functools import wraps

def timethis(func):
    '''
    Decorador que informa sobre el tiempo de ejecucion de una funcion
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
    

# Codigo de pruebas. Deberias decorar ese metodo para que, al llamarlo, imprimiera el tiempo de ejecucion
@timethis
def countdown(n):
    """
    Una simple cuenta atras
    """
    while n > 0:
        n -= 1
        
countdown(10000000)

# Acuérdate: ¿qué debería hacer en mi decorador para que aquí me informara correctamente de lo que hace mi método?
help(countdown)