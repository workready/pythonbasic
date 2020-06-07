# functools reduce + operator.add vs itertools.accumulate
import operator, functools, itertools

print(functools.reduce(operator.add, [1,2,3,4], 0)) # 10

# accumulate coge operator.add como segundo parámetro por defecto si no le pasamos nada
print(list(itertools.accumulate([1, 2, 3, 4]))) # [1, 3, 6, 10]