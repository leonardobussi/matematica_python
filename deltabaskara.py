import math
sair = 's'
while (sair == 's'):
    a = int(input("digite o valor de 'a': \n"))
    b = int(input("digite o valor de 'b': \n"))
    c = int(input("digite o valor de 'c': \n"))
    if( a != 0):
        print('\na = {0}\nb = {1}\nc = {2}\n'.format(a,b,c))
        print("------------------------------------------")
        print('b¨ - 4 × a × c')
        print('{0}¨ - 4 × {1} × {2}\n'.format(b,a,c))
        delta = ((b**2) - 4 * (a) * (c))
        print(delta)
        print("------------------------------------------")
        if (delta > 0):
            raiz = math.sqrt(delta)
            raiz2 = (math.floor(raiz)) 
            print("raiz de {0} eh {1}\n".format(delta, raiz2))
            print("-------------------------------------------")
            x1 = ((- b) + (raiz2)) / (2 * a)
            print("valor do X1", x1)
            x2 = ((- b) - (raiz2)) / (2 * a)
            print("valor do X2", x2)
        elif(delta <= 0):
            x1 = ((- b) + (raiz2)) / (2 * a)
            print("valor do X1", x1)
            x2 = ((- b) - (raiz2)) / (2 * a)
            print("valor do X2", x2)
    else:
        print("imposivel resolver pois nao se trata de equaçao do segundo grau")
        print("------------------------------------------")
    sair = input ("se quiser repetir digite o 's' ")    