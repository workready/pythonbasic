
# Crear un diccionario es igual de sencillo que un set
a_dict = {'server': 'server.com', 'database': 'MySQL'}
print(a_dict)   # {'database': 'MySQL', 'server': 'server.com'}

# Podemos acceder a los elementos de un diccionario usando indexación tipo array
print(a_dict['server']) # server.com
print(a_dict['database'])   # MySQL

# Se pueden añadir todos los elementos que se quiera a un diccionario. Y también podemos modificar los existentes
a_dict['user'] = 'Jorge'
a_dict['database'] = 'PostgreSQL'
print(a_dict)   # {'database': 'PostgreSQL', 'user': 'Jorge', 'server': 'server.com'}

# Se pueden mezclar elementos de diferentes tipos en un diccionario
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

print(SUFFIXES[1000])   # ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
print(SUFFIXES[1024])   # ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']