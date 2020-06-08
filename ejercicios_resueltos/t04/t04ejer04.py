import math

# En este ejercicio estamos implementando la Criba de Eratóstenes
# https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes

def is_prime(number):
    """
        Para determinar si un número n es primo, vemos si es divisible entre
        los términos de 1 a sqrt(n). La explicación: https://stackoverflow.com/a/5811176/593722
    """
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(start):
    number = start
    while True:
        if is_prime(number):
            yield number
        number += 1


# De esta forma, nuestro jefe podría hacer una función como ésta para resolver el problema Euler 10
def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

        
# De esta otra forma, podríamos obtener los primos hasta 100, generando uno cada vez
def primos_hasta(n):
    for next_prime in get_primes(3):
        if next_prime < n:
            print(next_prime, end=' ')
        else:
            break

print(primos_hasta(100))