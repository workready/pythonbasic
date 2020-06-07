import time
from functools import wraps

def timethis(func):
    '''
    Decorador que informa sobre el tiempo de ejecucion de una funcion
    '''
    pass    # Tu codigo aqui
    

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