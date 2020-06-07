def func(**kwargs):
    print("Argumentos:")
    for k,v in kwargs.items():
        print("{0} => {1}".format(k, v))

func(a=134, b=543, c="sfds")