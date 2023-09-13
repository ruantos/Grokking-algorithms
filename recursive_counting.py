""" Função recursiva para contar a quantidade de elementos em um array"""
def counter(arr):
    """ Conta os elementos de um array recursivamente. """
    if len(arr) == 1:
        return 1
    elif len(arr) == 0:
        return 0
    return 1 + counter(arr[1:])


array = []
print(counter(array))
