# Pythonista, pero mejorable
cadenas = ['uno', 'dos', 'tres', 'esto', 'me', 'sobra']
(primero, segundo, tercero, *resto) = cadenas

print(primero)
print(segundo)
print(tercero)


# Bien, esto sí es pythonista 100%
cadenas = ['uno', 'dos', 'tres', 'esto', 'me', 'sobra']
(primero, segundo, tercero, *_) = cadenas

print(primero)
print(segundo)
print(tercero)