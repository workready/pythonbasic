class Numbers:
    pass    # Tu codigo aqui


# Pruebas
assert(Numbers.MULTIPLIER == 3.5)

n = Numbers(4, 4)
assert(n.add() == 8)
assert(Numbers.multiply(2) == 7.0)
assert(Numbers.substract(5, 3) == 2)
assert(n.value == (4, 4))
n.value = (8, 6)
assert(n.value == (8, 6))
del n.value

try:
    print(n.x)
except Exception as e:
    print(e)

try:
    print(n.y)
except Exception as e:
    print(e)
    