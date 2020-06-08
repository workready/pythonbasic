import os

def gcat(filenames):
    for filename in filenames:
        with open(filename) as f:
            for line in f:
                yield line


def ggrep(pattern, filenames):
    for filename in filenames:
        with open(filename) as f:
            for line in f:
                if pattern in line:
                    yield line



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

