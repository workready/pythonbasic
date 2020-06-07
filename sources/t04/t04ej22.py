# Ejemplo sencillo: cambiar claves por valores
a_dict = {'a': 1, 'b': 2, 'c': 3}

# A destacar la llamada a .items() para obtener los elementos del diccionario
print({value:key for key, value in a_dict.items()})