import functools

fib_function = lambda n:functools.reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

fib = [fib_function(n) for n in range(17)]
print(fib)