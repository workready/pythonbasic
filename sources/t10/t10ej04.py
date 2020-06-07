import numpy as np

lista = [ 1, 1+2j, True, 'aerodinamica', [1, 2, 3] ]
print(id(lista))    # El id que tenga. Algo como 1721240621384
lista.append('fluidos')
print(lista)    # [1, (1+2j), True, 'aerodinamica', [1, 2, 3], 'fluidos', 'fluidos']
print(id(lista))    # El mismo id

array = np.array([ 1, 1+2j, True, 'aerodinamica'])
print(id(array))    # El id que tenga. Algo como 1721240769440
array = np.append(array, 'fluidos')
print(array)    # ['1' '(1+2j)' 'True' 'aerodinamica' 'fluidos']
print(id(array))    # Un id nuevo