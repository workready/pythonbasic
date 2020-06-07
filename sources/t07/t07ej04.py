# Lo mismo pero con una list comprehension
def es_impar(x):
    return x % 2
print([x for x in range(10) if es_impar(x)])