import numpy as np

# Generamos matriz de numeros aleatorios
M = np.random.rand(3,3)


# Salvamos la matriz en formato interno de numpy
np.save("random-matrix.npy", M)

!file random-matrix.npy # random-matrix.npy: data

# Podemos volver a cargar el fichero
np.load("random-matrix.npy")    # Veriamos la salida del fichero importado