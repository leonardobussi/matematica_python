import numpy as np
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("digite um valor para [{0}], [{1}] ".format(linha,coluna)))
print()
for l in range(0, 3):
    for c in range(0, 3):
        matrizz[l][c] = int(input("digite um valor para [{0}], [{1}] ".format(l,c)))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print({matriz[linha][coluna]}, end='')
    print()
print()
for l in range(0,3):
    for c in range(0,3):
        print({matriz[l][c]}, end='')
    print()
s = np.matmul(matriz,matrizz)
print()
print(s)
