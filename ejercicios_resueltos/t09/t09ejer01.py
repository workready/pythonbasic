import multiprocessing

# Funcion a ejecutar con multiproceso
def worker(num):
    return num*2

# Lista de numeros con los que trabajar
nums = [1,2,3,4,5,6,7,8,9]

values = None

# OJO: no quitar el main. En Windows, cada proceso hijo creado hace un import
# otra vez del módulo actual (este fichero en si). Al hacer el import, si no
# hay ningún main, se ejecuta todo el código del tirón. Y al intentar ejecutar
# varias veces el pool, peta
# Ver: https://stackoverflow.com/a/34223666

if __name__ == "__main__":
	# En values obtendremos el resultado de aplicar worker a la lista, utilizando un pool de 2 procesos
	# Tu codigo aqui
	p = multiprocessing.Pool(2)
	values = p.map(worker,nums) 

	p.close() 
	p.join()
	    

	assert(values == [2, 4, 6, 8, 10, 12, 14, 16, 18])
	print(values)