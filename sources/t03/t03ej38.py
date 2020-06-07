def func(*args, **kwargs):
    print ("Args:")
    for arg in args:
        print(arg)

    print ("Kwargs:")
    for k,v in kwargs.items():
        print("{0} => {1}".format(k, v))

func(2342, 43534, 5645, x=456, y=3)