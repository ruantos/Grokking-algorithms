""" The longest commmon substring and the longest common subsequence"""

def max(table):
    maior_valor = table[0][0]  
    
    for linha in table:
        for celula in linha:
            if celula > maior_valor:
                maior_valor = celula

    return maior_valor


def substring(table, wA, wB):
    for i in range(len(wA)):
        for j in range(len(wB)):
            if wA[i] == wB[j] and i != 0 and j != 0:
                table[i][j] = table[i - 1][j -1] + 1
            else:
                table[i][j] = 0
    return max(table)


A = "fish"
B = "hish"
tabela = [[0 for i in range(len(B))] for i in range(len(A))]
print(substring(tabela, A, B))
print(tabela)

