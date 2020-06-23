matriz = [[0, 0], [0, 0]]
for linha in range(0, 2):
    for coluna in range(0, 2):
        matriz[linha][coluna] = int(input("digite um valor para [{0}], [{1}] ".format(linha,coluna)))
for linha in range(0, 2):
    for coluna in range(0, 2):
        print({matriz[linha][coluna]}, end='')
    print()
principal = matriz[0][0] * matriz [1][1]
secundaria = matriz[0][1] * matriz[1][0]
d = principal - secundaria
print("diagonal principal deu: {0}".format(principal))
print("diagonal segundaria deu: {0}".format(secundaria))
print("o resultado da matriz D deu:{0}".format(d))
print("-"*30)
n1 = int(input("digite o primeiro numero do termo independente "))
n2 = int(input("digite o segundo numero do termo independente  "))
print("[{0}, {1}]\n[{2}, {3}]".format(n1,matriz[0][1],n2,matriz[1][1]))
e = n1 * matriz[1][1]
f = matriz[0][1] * n2
g = e - f
print("diagonal principal de Dx deu: {0}".format(e))
print("diagonal secundaria de Dx deu: {0}".format(f))
print("resultado de Dx deu: {0}".format(g))
print("-"*30)
print("[{0}, {1}]\n[{2}, {3}]".format(matriz[0][0],n1,matriz[1][0],n2))
h = matriz[0][0] * n1
i = n2 * matriz[1][0]
n = h - i
print("diagonal principal de Dy deu: {0}".format(e))
print("diagonal secundaria de Dy deu: {0}".format(f))
print("resultado de Dy deu: {0}".format(g))
print()
if (d == 0) and (g == 0) and (n == 0):
    print("sistema indeterminado impossivel")
if (d == 0) and (g != 0) and (n != 0):
    print("sistema impossivel")
if (d != 0) and (g != 0) and (n != 0):
    resulx = g/d
    resuly = n/d
    print("DX {0} dividido por D {1} eh igual = {2}".format(g,d,resulx))
    print("DY {0} dividido por D {1} eh igual = {2}".format(n,d,resuly))
    print("sistema possivel determinado")
