""" Fatorial recursivo"""

def factorial(n):
    """ Fatorial recursivo"""
    if n < 2:
        return 1
    return n * factorial(n - 1)


N = 5
print(factorial(N))
