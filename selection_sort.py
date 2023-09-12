""" Selection sort é um algoritmo de ordenação de simples implementação 
com taxa de crescimento O(n²)."""

def search_lower(arr):
    """Procura o menor elemento em um array e retorna seu índice. """
    smallest = arr[0]
    smallest_indx = 0
    for indx in range(1, len(arr)):
        if arr[indx] < smallest:
            smallest = arr[indx]
            smallest_indx = indx
    return smallest_indx


def selection_sort(arr):
    """ Itera sobre o array, a cada iteração busca o menor elemento contido na lista, 
    o adiciona a nova lista e o remove da lista antiga"""
    sorted_arr = []
    for _ in range(len(arr)):
        smallest = search_lower(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


array = [5,1,3,2]
print(selection_sort(array))
