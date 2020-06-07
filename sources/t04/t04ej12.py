# En este ejercicio agruparemos nombres de personas por su longitud, usando itertools
import itertools
import os

# Context manager en acción. Atención a cómo obtenemos el directorio donde se encuentra el script, para que no haya errores en la ruta
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'nombres.txt')) as f:
    names = list(f)

    # Necesitamos eliminar el salto de línea al final de cada nombre leído del fichero
    # Esto es una list comprehension. Las veremos al final de este tema
    names = [name.rstrip() for name in names]

    # Esto es por si no estuviera el fichero
    #names = ['Paco', 'Julia', 'Javier', 'Sara', 'Jose','Gala', 'Jorge', 'Marta', 'Alex', 'Carmen']

    # Groupby genera, a partir de un iterable, iterables con elementos que devuelvan el mismo resultado al aplicarles una función
    # El problema es que el iterable se detiene cuando un elemento ya no devuelve el mismo resultado que el anterior, sin importar si
    # ya ha generado iterables que devuelvan ese mismo resultado.
    # En nuestro caso, si la lista de nombres no estuviera ordenada por longitud, crearía un iterable para 'Paco' (longitud 4),
    # otro iterable para 'Julia' y 'Javier' (longitud 5), luego otro para 'Sara' (longitud 4), etc. Lo interesante sería que
    # 'Paco' y 'Sara' fueran en el mismo iterable, pues tienen la misma longitud.
    # Para conseguir eso, ordenamos la lista mediante el mismo criterio que usaremos en la generación de iterables.
    # Ver lo que pasa si llamamos a groupby sobre 'names' a secas
    grupos = itertools.groupby(sorted(names, key=len), len)

    for n, it in grupos:
        print("Nombres con {0} letras:".format(n), end=' ')
        for name in it:
            print(name, end=' ')
        print()