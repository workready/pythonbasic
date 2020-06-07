import numpy as np

# Generamos matriz de numeros aleatorios
M = np.random.rand(3,3)

# La guardamos
np.savetxt("random_matrix.csv", M)

# Podemos incluso mostrar el contenido del fichero
!cat random_matrix.csv

# También podemos especificar el formato para las celdas al guardar
# Por ejemplo, limitamos cada celda a 5 decimales
np.savetxt("random_matrix.csv", M, fmt="%.5f")

!cat random_matrix.csv