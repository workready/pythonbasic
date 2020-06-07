# Operaciones típicas de conjuntos: in, union, intersection, difference, symmetric_difference
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
30 in a_set
31 not in a_set

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print(a_set.union(b_set))   # {1, 2, 195, 4, 5, 3, 6, 8, 9, 76, 12, 15, 17, 18, 21, 30, 51, 127}
print(a_set.intersection(b_set))    # {9, 2, 21, 12, 5}
print(a_set.difference(b_set))  # {195, 4, 76, 51, 30, 127}
print(a_set.symmetric_difference(b_set))    # {1, 3, 195, 6, 4, 8, 76, 15, 17, 18, 51, 30, 127}