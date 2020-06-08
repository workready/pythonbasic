veces = 0
palabra_correcta = "cacahuete"
palabra = ""

while palabra.lower() != palabra_correcta.lower() and veces < 10:
    palabra = input("A ver si adivinas la palabra. Te quedan {} intentos: ".format(10 - veces))
    if palabra.lower() == palabra_correcta.lower():
        print('¡La has adivinado!, la palabra es {}'.format(palabra_correcta.lower()))
        break
    veces = veces + 1
else:
    print("Lo sentimos, no la has adivinado :-(. La palabra era {}".format(palabra_correcta))