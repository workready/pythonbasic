import pandas as pd
import os

# Rutas a ficheros
user_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'users.txt')
ratings_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'ratings.txt')

# Cabeceras a tener en cuenta para usuarios
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']

# TODO: Lee el dataset de usuarios usando pd.read_table. De todos los posibles parámetros de la función, emplea los siguientes:
#   Obviamente, la ruta al fichero de datos de usuarios
#   engine='python'
#   names=userHeader
#   sep: el separador de columnas que se esté usando en el fichero de datos
#   header: ¿tiene cabecera el fichero de datos? Fíjate en los ejemplos del tema para saber cómo gestionar la situación

# Tu código aquí <1>

# Cabeceras para tener en cuenta en ratings
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']

# TODO: Lee el fichero de ratings igual que leíste el fichero de usuarios
# Tu codigo aqui


# TODO: Mezcla ambos datasets. Seguro que hay una función que te hace la mezcla, detectando el campo común como enganche...
# Tu código aquí: <2>

# Imprime las 10 primeras posiciones del resultado de la mezcla
print('# Merge tables users + ratings by user_id field')
print(merger_ratings_users[:10])