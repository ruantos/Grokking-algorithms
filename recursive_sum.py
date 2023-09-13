""" Implementação de um algoritmo de soma dos elementos de um array de forma recursiva."""
def total_sum(array):
    """soma de vetores por recursão. Usa a técnica divide and conquer para diminuir
    o array em partes menores de si mesmo até chegar no caso base."""

    # Caso base, array sem elemento.
    if len(array) == 0:
        return 0
    # Soma o primeiro elemento com o resto do array
    return array[0] + total_sum(array[1:])


arr = [1,2,3,4,5]
print(total_sum(arr))
