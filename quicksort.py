""" Implementação do algoritmo de ordenação Quicksort. Algoritmo eficiente com O(n log n)"""

def qsort(array):
    """ Função de ordenação de arrays com técnica Divide and Conquer. """

    # Caso base
    if len(array) < 2:
        return array

    # Caso recursivo
    pivot = array[0]

    # Lista dos elementos menores que o pivot
    smallest = [int(i) for i in array[1:] if i < pivot]
    # Lista dos elementos maiores que o pivot
    greatest = [int(i) for i in array[1:] if i > pivot]

    # menores ordenados + pivot + maiores ordenados
    return qsort(smallest) + [pivot] + qsort(greatest)


arr = [3,6,7,1,10,42,14]
print(qsort(arr))
