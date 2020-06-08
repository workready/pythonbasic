class Numbers:
    MULTIPLIER = 3.5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a

    @staticmethod
    def substract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, xy_tuple):
        self.x, self.y = xy_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y



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
    