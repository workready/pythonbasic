import inspect

def info(obj, also_privates=True): 
    """
        Imprime todos los metodos del objeto y sus docstrings.
        Acepta modulos, clases, listas, diccionarios y cadenas
    """
    methodList = []
    
    # Tu codigo aqui
    
    for desc in methodList:
        print(desc)

class Punto:
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y
        
    def foo(self):
        """Metodo absurdo"""
        print("foo")

    def __metodo_oculto(self):
        """Metodo oculto"""
        print("Estoy oculto")
    

info(Punto)
print("+++++++++++++++++")
info(Punto, also_privates=False)