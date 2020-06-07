# Esto es una generator function. La podemos llamar hasta que se agote
def generatorFunction():
    # Ni siquiera necesitamos limite. Vamos a llamar a yield 3 veces, simulando lo que pasaría dentro del bucle
        yield 0
        yield 1
        yield 4


f = generatorFunction()
print(next(f))
print(next(f))
print(next(f))


# Esto es una *generator expression*. Como nos devuelve un iterador, podemos iterar sobre él hasta que se agote
lazy_squares = (x * x for x in [1, 2, 3, 4, 5, 6])

print(next(lazy_squares))
print(next(lazy_squares))
print(next(lazy_squares))
print(next(lazy_squares))
print(next(lazy_squares))