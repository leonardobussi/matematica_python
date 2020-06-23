matriz = [[0, 0,0], [0, 0,0]]
for linha in range(0, 2):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("digite um valor para [{0}], [{1}] ".format(linha,coluna)))
for linha in range(0, 2):
    for coluna in range(0, 3):
        print({matriz[linha][coluna]}, end='')
    print()
print()
for linha in range(0,3):
    for coluna in range(0,2):
        print({matriz[coluna][linha]}, end='')
    print()