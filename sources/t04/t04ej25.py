a_set = set(range(10))

# Creamos una set comprehension. El set no tiene porque está ordenado, aunque en este caso lo esté
print(sorted({x**2 for x in a_set if x % 2}))