import pandas as pd
import os

# Rutas a ficheros
user_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'users.txt')
ratings_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'ratings.txt')

# Cabeceras a tener en cuenta para usuarios
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']

# Lee el dataset de usuarios usando pd.read_table
users = pd.read_table('dataSet/users.txt', engine='python', sep='::', header=None, names=userHeader)

# Cabeceras para tener en cuenta en ratings
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']

# Lee el fichero de ratings igual que leíste el fichero de usuarios
ratings = pd.read_table('dataSet/ratings.txt', engine='python', sep='::', header=None, names=ratingHeader)

# TODO: Mezcla ambos datasets. Seguro que hay una función que te hace la mezcla, detectando el campo común como enganche...
merger_ratings = users.merge(ratings)

# Imprime las 10 primeras posiciones del resultado de la mezcla
print('# Merge tables users + ratings by user_id field')
print(merger_ratings[:10])