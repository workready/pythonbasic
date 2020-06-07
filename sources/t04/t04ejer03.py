import os

def gcat(filenames):
    pass    # Tu codigo aqui


def ggrep(pattern, filenames):
    pass    # Tu codigo aqui



# Codigo de pruebas para gcat
print("Fichero linea a linea")
print("-----------------------------")
for line in gcat([os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quijote.txt')]):
    print(line)
print("-----------------------------")

print()
print()

# Codigo de pruebas para ggrep
print("Lineas del fichero que contienen la palabra 'los'")
print("-----------------------------")
for l in list(ggrep("los", [os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quijote.txt')])):
    print(l)
print("-----------------------------")

