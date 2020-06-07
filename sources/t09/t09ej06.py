def writer():
    """Simula escribir datos que se le pasan en un socket, fichero, etc"""
    while True:
        w = (yield)
        print(w)


def writer_wrapper(coro):
    coro.send(None)  # Inicio la corrutina. Es equivalente a next(coro)
        
    while True:
        try:
            x = (yield)  # Capturo el valor que me envían
            coro.send(x)  # Y se lo paso al escritor
        except StopIteration:
            # Esto es opcional. Cuando el iterador se agota, los intentos por
            # continuar consumiéndolo fuerzan que lance esta excepción. La 
            # podemos capturar y hacer algo con ella
            pass    

# Comienza el juego
w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # Inicio la corrutina
for i in range(4):
    wrap.send(i)