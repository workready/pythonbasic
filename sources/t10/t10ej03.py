import numpy as np

lista = [ 1, 1+2j, True, 'aerodinamica', [1, 2, 3] ]
print(lista)   # [1, (1+2j), True, 'aerodinamica', [1, 2, 3]]

array = np.array([ 1, 1+2j, True, 'aerodinamica'])
print(array) # array(['1', '(1+2j)', 'True', 'aerodinamica'], dtype='<U64')