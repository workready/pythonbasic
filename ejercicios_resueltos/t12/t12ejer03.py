import pandas as pd
import numpy as np
import os

def cloneDF(df):
    """Devuelve una copia del dataframe que se le pasa como parámetro"""
    return pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy()).convert_objects(convert_numeric=True)


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

# La primera pivot table de ejemplo. Las otras dos las tendrás que hacer tú...
df_1 = cloneDF(mergeMovies)
df_1 = df_1.pivot_table(index=['movie_id', 'title'], values=['rating', 'age'])
print('\nColumns(movie_id + title) to Index and avg by values')
print(df_1[:5])

df_2 = cloneDF(mergeMovies)
df_2 = df_2.pivot_table(index=['movie_id', 'title'], values=['rating'], aggfunc=[np.sum, np.size, np.mean])
print('\nColumns(movie_id + title) to Index and specific functions by values')
print(df_2[:5])


df_3 = cloneDF(mergeMovies)
df_3 = df_3.pivot_table(index=['movie_id', 'title'], values=['rating'], columns=['gender'], aggfunc=[np.mean], fill_value=-1, margins=True)
print('\nColumns(movie_id + title) to Index and avg rating applied by gender')
print(df_3[:5])
