class SpamException(Exception):
    pass

def writer():
    """Simula escribir datos que se le pasan en un socket, fichero, etc"""
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print(w)

def writer_wrapper(coro):
    coro.send(None)  # Inicio la corrutina. Es equivalente a next(coro)
    while True:
        try:
            x = (yield)  # Capturo el valor que me envían
            coro.send(x)  # Y se lo paso al escritor
        except StopIteration:
            pass    # Capturo la señal de finalización, cuando me dejan de mandar datos

# Comienza el juego
w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # Inicio la corrutina

# Vamos a hacer saltar la excepción en el escritor
for i in [0, 1, 2, 'spam', 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        wrap.send(i)

