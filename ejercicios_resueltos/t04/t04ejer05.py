# Aqui tu funcion
def palindromos(lista):
    return [string for string in lista if ''.join(string.lower().split()) == ''.join(string.lower()[::-1].split())]


# Lo puedes probar con esta lista
lista = [
    "Añora la Roña",
    "Como que moc",
    "Anita lava la tina",
    "Eva ya hay ave",
    "Yo no maldigo mi suerte porque minero naci"
]

print(palindromos(lista))