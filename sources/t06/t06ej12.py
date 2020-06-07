# Ejemplo de uso de función estática, no recibe ningún argumento, pero hace alguna operación útil dentro de la clase
class Math:
    @staticmethod
    def es_par(n):
        return not n % 2

m = Math()

# La puedo llamar desde la clase o desde una instancia
print(m.es_par(2))
print(Math.es_par(3))