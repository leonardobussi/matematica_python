print("exemplos\n")
print("-----------------------------------------------------------")
print("formato 1º Ax + Bx + C = 0 (funcionando) ")
print("-----------------------------------------------------------")
print()
print("formato 2º Ax + 1 = Bx + 1 (funcionando) ")
print("-----------------------------------------------------------")
print()
print("formato 3º f(x) Ax + b (funcionando) ")
print("-----------------------------------------------------------")
print()
print("formato 4º fracao Ax = bx + c (funcionando) ")
print("                 ---   ---                                 ")
print("                  1     1                                  ")
print("-----------------------------------------------------------")
print()
simnao = str(input("digite o numero: 1/2/3/4 "))
print()
if (simnao == '1'):
    a = int(input("digite o valor de ax: "))
    b = int(input("digite o valor de bx: "))
    c = int(input("digite o valor de c:  "))
    print()
    print("{0}X + {1}X + {2} = 0 ".format(a,b,c))
    cc = c*(-1)
    print("{0}X + {1}X = {2} ".format(a,b,cc))
    ab = a + b
    print("{0}X = {1} ".format(ab,cc))
    if (ab > 0) and (cc > 0):
        div = cc / ab
        if (cc > ab):
            print("X = {0} ".format(div))
        else:
            print("fracao {0} / {1}\nresul da fraçao {2}".format(cc,ab,div))
    elif(ab == 0) and (cc >= 0):
        print("X = {0} ".format(cc))
    elif (ab < 0) and (cc < 0):
        cde = cc * (-1)
        abc = ab * (-1)
        if (cde < abc):
            print("fraçao {0} / {1}".format(cde,abc))
            div = cde / abc
            print("divisao da fracao deu: {0}".format(div))
        else:
            div = cde / abc
            print("X = {0}".format(div))
            print("o numero independente sobre o dependente deu: {0} / {1}".format(cde,abc))
    else:
        if (cc > ab):
            div = cc / ab
            print("X = {0}".format(div))
        else:
            if (ab == 0):
                print("resultado X = {0}".format(cc))
            else:
                print("fracao {0}/{1}".format(cc,ab))
                print("resultado X = {0}".format(cc/ab))

            ######################################################

elif (simnao == '2'):
        a = int(input("digite o valor de ax: "))
        n1 = int(input("digite o valor independente "))
        b = int(input("digite o valor de bx: "))
        n2 = int(input("digite o valor independente "))
        print("{0}X + {1} = {2}X + {3}".format(a,n1,b,n2))
        n11 = n1 * (-1)
        bb = b * (-1)
        print("{0}X + {1}X = {2} + {3}".format(a,bb,n2,n11))
        ab = a + bb
        n = n2 + n11
        print("{0}X = {1} ".format(ab,n))
        if (ab < 0) and (n < 0):
            abb = ab * (-1)
            nnn  = n * (-1)
            print("{0} × (-1)\n{1} × (-1) ".format(ab,n))
            print("{0}X = {1}".format(abb,nnn))
            if (nnn >= abb):
                div = nnn / abb
                print("{0} ÷ {1} = {2}".format(nnn,abb,div))
                print(" X = {0}".format(div))
            else: 
                divi = nnn / abb
                print("fracao {0}/{1} ".format(nnn,abb))
                print("a divisao da fracao deu: {0}".format(divi))
        elif (ab > 0) or (n > 0):
            if (n > ab):
                w = n / ab
                print("fracao {0}/{1}".format(n,ab))
                print("X = {0}".format(w))
            else:
                print("fracao {0}/{1}".format(n,ab))
                w = n / ab
                print("divisao da fracao deu: {0}".format(w))
        elif (ab == 0) and (n != 0):
            print("X = {0}".format(n))
        else:
            print("impossivel resolver")
        ######################################
elif (simnao == '3'):
        a = int(input("digite o valor de ax: "))
        c = int(input("digite o valor de c:  "))
        print("{0}X + {1} = 0 ".format(a,c))
        bb = c * (-1)
        print("{0}x = {1}".format(a,bb))
        if (a < 0) and (bb < 0):
            v = (a * (-1))
            vv = (bb * (-1))
            print("{0}X = {1}".format(v,vv))
            print("fracao {0}/{1}".format(vv,v))
            div = vv/v
            print("X = {0}".format(div))
        else:
            ddd = bb / a
            print("{0}/{1}".format(bb,a))
            print("X = {0}".format(ddd))
        ######################################
elif (simnao == '4'):
        a = int(input("digite o valor de aX "))
        da = int(input("'a' dividido por "))
        b = int(input("digite o valor de bX: "))
        db = int(input("'b' dividido por "))
        c = int(input("digite o valor de c "))
        print("\n\n")
        print("{0}X = {1}X + {2} ".format(a,b,c))
        print("---  ---        ")
        print("{0}     {1}       ".format(da,db))
        print("\n\n")
        mmc = da * db * 1
        divda = mmc / da
        divdb = mmc / db
        aa =  int(divda * a)
        bb =  int(divdb * b)
        cc = int((mmc / 1) * c)
        print("{0}X = {1}X + {2}".format(aa,bb,cc))
        bbb = bb * (-1)
        print("{0}X + {1}X = {2} ".format(aa,bbb,cc))
        ao = int(aa + bbb)
        print("{0}X = {1}".format(ao,cc))
        if (ao < 0) and (cc < 0):
            g = ao * (-1)
            h = cc * (-1)
            print("{0}X = {1}".format(g,h))
            if (g > h):
                print("fracao X = {0}/{1}".format(h,g))
                divfra = int(h/g)
                print("divisao da fracao X = {0}".format(divfra))
            else:
                divfra = int(h/g)
                print("divisao da fracao X = {0}".format(divfra))
        elif(ao > 0) or (cc > 0):
            if (ao > cc):
                print("fracao {0}/{1}".format(cc,ao))
            else:
                gf = int(cc/ao)
                print("resultado deu: X = {0}".format(gf))
        else:
            print("X = {0}".format(cc))  
else:
    print("numero e caracter desconhecido")
