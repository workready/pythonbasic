import numpy as np

lista = list(range(0,100000))
array = np.arange(0, 100000)

%%timeit
sum(lista)  # Pulsamos ENTER dos veces para que empiece a medir tiempo

%%timeit
np.sum(array)   # Pulsamos ENTER dos veces para que empiece a medir tiempo