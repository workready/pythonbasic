# Python añadirá internamente el nombre de la clase delante de __baz
class Foo(object):
    def __init__(self):
        self.__baz = 42

    def foo(self):
        print(self.__baz)

# Como el método __init__ empieza por __, en realidad será Bar__init__, y el del padre Foo__init__. Así existen por separado
class Bar(Foo):
    def __init__(self):
        super().__init__()
        self.__baz = 21

    def bar(self):
        print(self.__baz)


x = Bar()

x.foo() # 42, porque el método imprime Foo__baz
x.bar() # 21, porque el método imprime Bar__baz

# Podemos ver los miembros "mangleados" que tiene la instancia x
print(x.__dict__) # {'_Bar__baz': 21, '_Foo__baz': 42}

