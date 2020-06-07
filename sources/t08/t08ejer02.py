import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG)

def logged(level, message):
    '''
    Añadiendo logging a una funcion. level es el
    nivel de logging, y message es el mensaje de log
    '''
    pass    # Tu codigo aqui
    

# Codigo de pruebas
@logged(logging.DEBUG, "Esto es un mensaje de debug")
def add(x, y):
    return x + y

@logged(logging.CRITICAL, "Esto es un mensaje critico")
def spam():
    print('Spam!')

# Si ponemos el nivel de log a INFO, el mensaje de DEBUG no debería salir

spam()
# Salida esperada:
"""
CRITICAL:spam:Esto es un mensaje critico
Spam!
"""

add(3, 4)
# Salida esperada: DEBUG:add:Esto es un mensaje de debug