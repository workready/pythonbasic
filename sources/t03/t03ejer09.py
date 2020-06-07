# Estos son los módulos que necesitas
import datetime
import calendar
import locale

def get_today_as_string():
    """
        Funcion que me dice el día de la semana que es hoy, en formato string.
        Pequeña guia de implementación:

        1. Obtén el día de la semana que es hoy, en formato entero (1, 2, 3, etc). Usa datetime.
        2. Obtén en una lista, los días de la semana en español en formato string. Usa calendar y locale.
        3. Usa el resultado de 1 para indexar el array de 2

        @returns: "Lunes", "Martes"...
    """
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    pass    # Tu codigo aqui


print("Hoy es {}".format(get_today_as_string()))