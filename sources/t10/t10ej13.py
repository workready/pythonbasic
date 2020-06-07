import numpy as np

!head sources/stockholm_td_adj.tsv

"""
    La salida será

1800  1  1    -6.1    -6.1    -6.1 1
1800  1  2   -15.4   -15.4   -15.4 1
1800  1  3   -15.0   -15.0   -15.0 1
1800  1  4   -19.3   -19.3   -19.3 1
1800  1  5   -16.8   -16.8   -16.8 1
1800  1  6   -11.4   -11.4   -11.4 1
1800  1  7    -7.6    -7.6    -7.6 1
1800  1  8    -7.1    -7.1    -7.1 1
1800  1  9   -10.1   -10.1   -10.1 1
1800  1 10    -9.5    -9.5    -9.5 1
"""

# Cargamos los datos en un array de numpy
data = np.genfromtxt('sources/stockholm_td_adj.tsv')

# Mostramos sus dimensiones. Como veremos en el siguiente tema, podemos graficarlos con matplotlib
data.shape  # (77431, 7)