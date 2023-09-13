""" Função recursiva para encontrar o maior elemento em um array """
def maximum(arr):
    """ retornará o maior elemento. """
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub = maximum(arr[1:])
    return arr[0] if arr[0] > sub else sub

array = [1,10,3,4,5]
print(maximum(array))
