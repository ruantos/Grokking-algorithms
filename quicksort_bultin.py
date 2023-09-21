"""Quicksort com função partition bem definida. """
from time import time

def partition(array, start, end):
    """ Rearranjo dos elementos"""
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[end], array[i] = array[i], array[end]
    return i


def quicksort(array, start=0, end=None):
    """ Função de ordenação de vetores com estratégia DAC"""
    if end is None:
        end = len(array) -1
    if start < end:
        piv = partition(array, start, end)

        quicksort(array, start, piv - 1)
        quicksort(array, piv + 1, end)




arr = [3,3,6,7,1,10,42,14]
tic = time()
quicksort(arr)
print(arr)
toc = time()
print(f'Tempo de execução {toc - tic}s')
