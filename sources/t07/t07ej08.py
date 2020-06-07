# Pruebas con any y all
print(any([0, False, None, True]))  # True
print(any([0, False, None, "", [], {}, ()])) # False

print(all([1, True, "hola", [1, 2, 3], {'foo': 'bar'}, (5, 6, 7)])) # True
print(all([0, True, "hola", [1, 2, 3], {'foo': 'bar'}, (5, 6, 7)])) # False