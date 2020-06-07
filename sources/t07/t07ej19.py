# Ejemplo de uso de expresión lambda en Python
a = [1, 2, 3]
b = [4, 5, 6]
suma_cuadrados = lambda x, y: x**2 + y**2
print([suma_cuadrados(x, y) for x, y in zip(a, b)])