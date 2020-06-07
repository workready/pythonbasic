# Corrutina
def minimize():
    try:
        # La primera vez que se llame a next(), el generador arrancará y se ejecutará hasta encontrar un yield. 
        # La llamada a next() es equivalente a send(none), de manera que se guardará None en current, 
        # y entonces parará, a esperas de la siguiente llamada
        current = yield

        # El resto de llamadas después del primer next() entrarán en el bucle. Con yield current recogemos el valor que nos llegue cada vez.
        while True:
            value = yield current
            current = min(value, current)
        
    except GeneratorExit:
        # Cuando alguien llame a close, implícita o explícitamente (ej: al terminar el programa), 
        # se lanzará la excepción GeneratorExit dentro del generador. Por supuesto, nosotros 
        # podemos capturar dicha excepción, y ejecutar cualquier tarea de limpieza necesaria dentro
        # de nuestro generador 
        print("Terminando corrutina")

# Construimos corrutina
it = minimize()

# La iniciamos
next(it)

# Le enviamos valores
print(it.send(10))      # min: 10
print(it.send(1))       # min: 1
print(it.send(1055))    # min: 1
print(it.send(-4))      # min: -4

it.close()  # Llamada explicita a close, aunque no es necesaria
