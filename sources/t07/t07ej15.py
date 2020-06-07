# Devolviendo funciones con functools.partial
import functools

def power(base, exponent):
    return base**exponent;

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(square(8))    # 64
print(cube(5))  # 125