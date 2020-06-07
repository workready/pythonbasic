import math

print("Hola gente del curso de Python")
print("¿Cuántos sois hoy en clase?")

number = input()
number = int(number)
root = math.sqrt(number)

print("¡Ufff!, sois un montón! espero que aprendáis mucho")
print("Por cierto, la raiz de {} es {}".format(number, root))
