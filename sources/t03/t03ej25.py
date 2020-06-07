# Mal, esto no es pythonista
color = 'verde'
if color == 'verde' or color == 'rojo' or color == 'azul':
    print('El {0} es un color primario'.format(color))


# Bien, esto es pythonista
color = 'verde'
if color in ('verde', 'rojo', 'azul'):
    print('El {0} es un color primario'.format(color))