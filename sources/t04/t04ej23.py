# Intentamos lo mismo, pero teniendo una lista como valor en lugar de un número
a_dict = {'a': [1, 2, 3], 'b': 4, 'c': 5}

print({value:key for key, value in a_dict.items()})