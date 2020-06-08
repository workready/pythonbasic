# Tu codigo aqui
with open("pep8.py") as f:
    for i,line in enumerate(f):
        if line[0] == "#":
            print("La línea {} del fichero empieza por un comentario".format(i))