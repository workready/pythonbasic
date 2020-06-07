# Uso de operator.add + functools.reduce
import operator, functools

print(functools.reduce(operator.add, [1,2,3,4], 0)) # 10
print(sum([1, 2, 3, 4]))    # 10