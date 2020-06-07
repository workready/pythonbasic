import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quijote.txt')) as f:
    for i,line in enumerate(f):
        if len(line) > 60:
            print("La línea {} del fichero tiene más de 60 caracteres".format(i))