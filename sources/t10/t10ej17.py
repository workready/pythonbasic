import numpy as np

x = np.arange(0, 10, 0.5)
mask = (5 < x) * (x < 7.5)

# Uso de where
indices = np.where(mask)    # (array([11, 12, 13, 14]),)
print(x[indices])   # [ 5.5  6.   6.5  7. ]

# Uso de take
v2 = np.arange(-3,3)
v2  # array([-3, -2, -1,  0,  1,  2])

row_indices = [1, 3, 5]
v2.take(row_indices)    # array([-2,  0,  2])


# Choices permite elegir de varios arrays
which = [1, 0, 1, 0]
choices = [[-2,-2,-2,-2], [5,5,5,5]]

np.choose(which, choices)   # array([ 5, -2,  5, -2])