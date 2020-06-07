import multiprocessing

# Funcion a ejecutar con multiproceso
def worker(num):
    return num*2

# Lista de numeros con los que trabajar
nums = [1,2,3,4,5,6,7,8,9]

values = None

# En values obtendremos el resultado de aplicar worker a la lista, utilizando un pool de 2 procesos
# Tu codigo aqui

assert(values == [2, 4, 6, 8, 10, 12, 14, 16, 18])
print(values)