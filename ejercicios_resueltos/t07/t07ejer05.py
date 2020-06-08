import functools

frases = ['Jorge es un tipo excepcional.',
             'Todo el mundo adora a Jorge, porque Jorge es genial.',
             'Jorge llora frecuentemente en su rincón de llorar cuando nadie le ve.']

jorge_count = functools.reduce(lambda a, x: a + x.count('Jorge'),
                   frases,
                   0)

print(jorge_count)