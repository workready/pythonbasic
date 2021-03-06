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

# TODO: Lee el dataset de usuarios usando pd.read_table. De todos los posibles parámetros de la función, emplea los siguientes:
#   Obviamente, la ruta al fichero de datos de usuarios
#   engine='python'
#   names=userHeader
#   sep: el separador de columnas que se esté usando en el fichero de datos
#   header: ¿tiene cabecera el fichero de datos? Fíjate en los ejemplos del tema para saber cómo gestionar la situación

# Tu código aquí

# Cabeceras para tener en cuenta en ratings
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']

# TODO: Lee el fichero de ratings igual que leíste el fichero de usuarios
# Tu codigo aqui


# Cabeceras para películas
movieHeader = ['movie_id', 'title', 'genders']


# TODO: Lee el fichero de películas igual que los anteriores
# Tu codigo aqui


# TODO: Mezcla los 3 datasets. Seguro que hay una función que te hace la mezcla, detectando el campo común como enganche...
# Tu código aquí:

# La primera pivot table de ejemplo. Las otras dos las tendrás que hacer tú...
df_1 = cloneDF(mergeMovies)
df_1 = df_1.pivot_table(index=['movie_id', 'title'], values=['rating', 'age'])
print('\nColumns(movie_id + title) to Index and avg by values')
print(df_1[:5])

df_2 = cloneDF(mergeMovies)

# Crea la pivot_table aqui...
print('\nColumns(movie_id + title) to Index and specific functions by values')
print(df_2[:5])


df_3 = cloneDF(mergeMovies)

# Crea la pivot table aqui...
print('\nColumns(movie_id + title) to Index and avg rating applied by gender')
print(df_3[:5])