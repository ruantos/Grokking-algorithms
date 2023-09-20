""" Implementação do algoritmo de ordenação Quicksort. 
Um dos algoritmos de ordenação mais eficientes com O(n log n).
Superando Mergesort e HeapSort. Porém, em seu pior caso é O(n²).
O pior caso ocorre quando o pivot se encontra em um dos extremos do array"""
import time
from random import randint

def qsort(array):
    """ Função de ordenação de arrays com técnica Divide and Conquer. """

    # Caso base
    if len(array) < 2:
        return array

    # Caso recursivo
    # pivot = valor aleatório.
    pivot = array[randint(0, len(array) -1)]
    array.remove(pivot)

    smallest = [int(i) for i in array if i <= pivot]
    # Lista dos elementos menores que o pivot
    # Lista dos elementos maiores que o pivot
    greatest = [int(i) for i in array if i > pivot]

    # menores ordenados + pivot + maiores ordenados
    return qsort(smallest) + [pivot] + qsort(greatest)


tic = time.time()

arr = [3,3,6,7,1,10,42,14]
print(qsort(arr))

toc = time.time()
print(f"Tempo de execução n1: {toc - tic}")

