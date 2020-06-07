# Ejemplo de lanzamiento y captura de excepción
class Triangulo:
   def __init__(self, base, altura):
       if base <= 0:
           raise ValueError("La base del triángulo tiene que medir más de 0")

       if altura <= 0:
           raise ValueError("La altura del triángulo tiene que medir más que 0")


t = Triangulo(2, 3)

# Capturamos la excepción
try:
   t = Triangulo(-2, 4)
except ValueError as e:
   print(e)

# Esto se ejecuta siempre, tanto si salta la excepción como si no. No es obligatorio ponerlo
finally:
   print("Programa terminado")