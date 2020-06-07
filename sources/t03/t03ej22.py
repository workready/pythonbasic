# Mal, esto no es pythonista
frutas = {'verde': 'pera', 'amarilla': 'plátano', 'roja': 'fresa'}
if 'azul' in frutas:
    fruta_azul = frutas['azul']
else:
    fruta_azul = 'piña'

print(fruta_azul)


# Esto si es pythonista
frutas = {'verde': 'pera', 'amarilla': 'plátano', 'roja': 'fresa'}

fruta_azul = frutas.get('azul', 'piña')
print(fruta_azul)