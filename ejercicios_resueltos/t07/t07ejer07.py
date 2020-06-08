import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args)/len(args)
d = lambda s: "".join(set(s))

# Las lambdas son útiles en combinación con map o filter
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7, 8, 9])))