def cumple_normativa(tiempo, descanso):
    """
        Decide si los criterios establecidos para un determinado examen pasan la normativa o no.
        @param tiempo: tiempo en horas
        @param descanso: booleano que define si hay descanso o no
        @return: True si se cumple la normativa. False en caso contrario
    """
    return True if tiempo <= 3 else descanso


assert(cumple_normativa(4, True) is True)
assert(cumple_normativa(5, False) is False)