""" Implementação da busca binária. """

def binary_search(arr, elem):
    """ Binary Search é um algoritmo de busca de tempo O(log n). 
    Porém, só pode ser aplicado em listas ordenadas. 
    Recebe por parâmetros a lista ordenada e o elemento que está sendo buscado. 
    Caso encontrado, retornará o indíce do elemento, caso contrário -1. """
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]
        if guess < elem:
            start = mid + 1
        elif guess > elem:
            end = mid - 1
        else:
            return mid
    return -1


array = [int(i) for i in range(100)]
X = 75

print(binary_search(array, X))
