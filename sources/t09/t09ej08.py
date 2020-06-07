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
    coro.send(None)  # Inicio la corrutina.
    while True:
        try:
            try:
                x = (yield)
            except Exception as e:   # Capturo la excepción que me mandan
                coro.throw(e)   # Se la mando al writer
            else:
                coro.send(x)    # Le mando al writer el valor
        except StopIteration:   # Capturo final de la secuencia
            pass

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

