import pandas as pd
import os

# Rutas a ficheros
user_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'users.txt')
ratings_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'ratings.txt')
movies_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dataSet', 'movies.txt')

# Cabeceras a tener en cuenta para usuarios
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']

# Lee el dataset de usuarios usando pd.read_table
users = pd.read_table('dataSet/users.txt', engine='python', sep='::', header=None, names=userHeader)

# Cabeceras para tener en cuenta en ratings
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']

# Lee el fichero de ratings igual que leíste el fichero de usuarios
ratings = pd.read_table('dataSet/ratings.txt', engine='python', sep='::', header=None, names=ratingHeader)


# Cabeceras para películas
movieHeader = ['movie_id', 'title', 'genders']


# Lee el fichero de películas igual que los anteriores
movies = pd.read_table('dataSet/movies.txt', engine='python', sep='::', header=None, names=movieHeader)


# Mezcla los 3 datasets. Seguro que hay una función que te hace la mezcla, detectando el campo común como enganche...
mergeMovies = movies.merge(users.merge(ratings))

info1000 = mergeMovies.ix[1000]

# Imprime la posición 1000 del resultado de la mezcla
print('Info of 1000 position of the table:')
print(info1000[:])
