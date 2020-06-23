a = int(input("digite o a: "))
b = int(input("digite o b: "))
c = int(input("digite o c: "))
print("a raiz da funçao f(x) = {0}x {1}x  {2} = 0".format(a,b,c))
print("soma:    ___ + ___ = {0}".format(b))
print("produto: ___ . ___ = {0}".format(c))
print("voce tera que tentar no chute ")
sair = 's'
while (sair == 's'):
    n1 = int(input("chute um numero:     "))
    n2 = int(input("chute outro numero:  "))
    rs = (n1) + (n2)
    rp = (n1) * (n2)
    if (rs == abs(b)) and (rp == abs(c)) or  (rs == (b)) and (rp == (c)):
        print("{0} + {1} = {2} ".format(n1,n2,b))
        print("{0} × {1} = {2} ".format(n1,n2,c))
        print("as raizes sao:  {0} e {1}".format(n1,n2))
    else:
        print('nao deu certo, tente outra vez')
    sair = input("tentar s/n ")
    print("-----------------------------------") 