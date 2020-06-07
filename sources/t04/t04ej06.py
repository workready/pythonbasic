# 15 primeros dígitos de la secuencia de Fibonacci con comprehension list
fib = [0,1]
[fib.append(fib[-1] +fib[-2]) for ctr in range(15)]
print(fib)