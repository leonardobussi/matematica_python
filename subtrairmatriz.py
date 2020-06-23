    
class subtrair:   
    import numpy as np

    print('-=-'*20, '\nCONSTRUÇÃO DE MATRIZ Pt1\n', '-=-'*20)
    matriz = list()
    temp = list()
    nc = int(input('Número de colunas: '))
    nl = int(input('Número de linhas: '))
    print('~~'*20)
    for l in range(1, nl+1):
        for c in range(1, nc+1):
            temp.append(int(input(f'Digite um valor para linha {l}, coluna {c}: ')))
        matriz.append(temp)
        temp = list()
    print('~~'*20)
    for l in range(0, nl):
        for c in range(0, nc):
            print(f'{matriz[l][c]:^5}', end=' ')
        print()
    print('~~'*20)




    print('-=-'*20, '\nCONSTRUÇÃO DE MATRIZ Pt2\n', '-=-'*20)
    matriz1 = list()
    temp = list()
    nc = int(input('Número de colunas: '))
    nl = int(input('Número de linhas: '))
    print('~~'*20)
    for l in range(1, nl+1):
        for c in range(1, nc+1):
            temp.append(int(input(f'Digite um valor para linha {l}, coluna {c}: ')))
        matriz1.append(temp)
        temp = list()
    print('~~'*20)
    for l in range(0, nl):
        for c in range(0, nc):
            print(f'{matriz1[l][c]:^5}', end=' ')
        print()
    print('~~'*20)

    soma = np.array(matriz) - np.array(matriz1)
    print (soma)