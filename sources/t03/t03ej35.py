"""
Potencial error aquí. El valor por defecto de una función es evaluado una sola vez. Si dicho argumento es un objeto mutable,
como una lista o un diccionario, la función acumula los argumentos pasados en llamadas sucesivas
"""
def f(a, L=[]):
    L.append(a)
    return L

print (f(1))    # [1]
print (f(2))    # [1, 2]
print (f(3))    # [1, 2, 3]


# Si queremos evitar que se acumule el valor del argumento por defecto, lo podemos escribir así
def f(a, L=None):
    if not L:
        L = []
    L.append(a)
    return L

print (f(1))    # [1]
print (f(2))    # [2]
print (f(3))    # [3]