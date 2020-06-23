import math
print("\n─────────────────────")
print("| lim   ax² - bx - c |\n| X→t   ------------ |\n|       ax² - bx - c |\n|                    |   Opção nº 1")
print("---------------------")
print("| lim   ax² - bx     |\n| X→t   ------------ |\n|       x² - b      |\n|                    |   Opção nº 2")
print("---------------------")
print("| lim   ax² - bx    |\n| X→t   ------------ |\n|       ax² - bx -c  |\n|                    |   Opção nº 3")
print("─────────────────────\n")
opcao = int(input("digite o numero da opcao desejada: "))
if opcao == 1:
    a = int(input("digite o valor de 'a' "))
    b = int(input("digite o valor de 'b' "))
    c = int(input("digite o valor de 'c' "))
    print("───────Sobre───────")
    a2 = int(input("digite o valor de 'a' "))
    b2 = int(input("digite o valor de 'b' "))
    c2 = int(input("digite o valor de 'c' "))
    print("───────X→t───────")
    x = int(input("digite o valor de 't' "))
    xx = math.ceil(math.pow(x,2))

    aa = a*xx
    bb = b*x

    aa2 = a2*xx
    bb2 = b2*x

    res = ((aa) + (bb)) + (c)
    res2 = ((aa2) + (bb2)) + (c2)

    if res != 0 and res2 != 0:
        print(f"\nlim     {a}x² + {b}x + {c}           {a}.{x}² + {b}.{x} + {c}                {aa} + {bb} + {c}                     {res}     ")
        print(f"X→{x}  -------------------- =    --------------------- =    ----------------------- =    --------------")
        print(f"        {a2}x² + {b2}x + {c}            {a2}.{x}² + {b2}.{x} + {c2}              {aa2} + {bb2} + {c2}                     {res2}\n")

    elif res == 0 and res2 == 0:
        print(f"\nlim     {a}x² + {b}x + {c}           {a}.{x}² + {b}.{x} + {c}                {aa} + {bb} + {c}                     {res}     ")
        print(f"X→{x}  -------------------- =    --------------------- =    ----------------------- =    --------------")
        print(f"        {a2}x² + {b2}x + {c}            {a2}.{x}² + {b2}.{x} + {c2}              {aa2} + {bb2} + {c2}                     {res2}\n\n")
        
        in_x = x *(-1)
        div_c = math.ceil((c/in_x))
        div_c2 = math.ceil((c2/in_x))

        soma = (x) + (div_c)
        soma2 = (x) + (div_c2) 

        print(f"\nlim     {a}x² + {b}x + {c}         lim  (x | {in_x}).(x + {div_c})                {x} + {div_c}                         {soma}     ")
        print(f"X→-{x}  -------------------- =    x→{in_x} ---|----------------- =    ----------------------- =    --------------")
        print(f"        {a2}x² + {b2}x + {c}              (x | {in_x}).(x + {div_c2})              {x} + {div_c2}                            {soma2}\n\n")

    else:
        print("não ha solução disponivel no momento")
if opcao == 2:
    a = int(input("digite o valor de 'a' "))
    b = int(input("digite o valor de 'b' "))
    c = int(input("digite o valor de 'c' "))
    print("───────Sobre───────")
    b2 = int(input("digite o valor de 'b' "))
    print("───────X→t───────")
    x = int(input("digite o valor de 't' "))

    xx = math.ceil(math.pow(x,2))
    b22 = abs(b2)
    raiz = math.sqrt(b22)


    aa = (a*xx)
    bb = (b*x)


    res = ((aa) + (bb)) + (c)
    res2 = math.ceil((x) + (raiz))

    if res != 0 and res2 != 0:
        print(f"\nlim     {a}x² + {b}x + {c}           {a}.{x}² + {b}.{x} + {c}                {aa} + {bb} + {c}                     {res}     ")
        print(f"X→{x}  -------------------- =    --------------------- =    ----------------------- =    --------------")
        print(f"           x² + {b2}                  {x}² + {b2}                              {x} + {raiz}                     {res2}\n\n")

    elif res == 0 and res2 == 0:
        print(f"\nlim     {a}x² + {b}x + {c}           {a}.{x}² + {b}.{x} + {c}                {aa} + {bb} + {c}                     {res}     ")
        print(f"X→{x}  -------------------- =    --------------------- =    ----------------------- =    --------------")
        print(f"           x² + {b2}                  {x}² + {b2}                              {x} + {raiz}                     {res2}\n\n")
# terminar aqui        
        in_x = x *(-1)
        div_c = math.ceil((c/in_x))
        raizz = raiz * (-1)
        soma = (x) + (div_c)
        soma2 = (x) + (raizz)
        soma3 = (x) + (raiz)
        if b2 < 0:
            
            print(f"\nlim     {a}x² + {b}x + {c}         lim  (x | {in_x}).(x + {div_c})                {x} + {div_c}                         {soma}     ")
            print(f"X→{x}  -------------------- =    x→{in_x} ---|----------------- =    ----------------------- =    --------------")
            print(f"          x² + {b2}                  (x | {raiz}).(x + {raizz})              {x} + {raizz}                            {soma2}\n\n")
        
        
        else:    
            print(f"\nlim     {a}x² + {b}x + {c}         lim  (x | {in_x}).(x + {div_c})                {x} + {div_c}                         {soma}     ")
            print(f"X→{x}  -------------------- =    x→{in_x} ---|----------------- =    ----------------------- =    --------------")
            print(f"         x² + {b2}                  (x | {raiz}).(x + {raiz})              {x} + {raiz}                            {soma3}\n\n")
    
    else:
        print("não ha solução disponivel no momento")
elif opcao == 3:
    a = int(input("digite o valor de 'a' "))
    b = int(input("digite o valor de 'b' "))
    print("───────Sobre───────")
    a2 = int(input("digite o valor de 'a' "))
    b2 = int(input("digite o valor de 'b' "))
    c2 = int(input("digite o valor de 'c' "))
    print("───────X→t───────")
    x = int(input("digite o valor de 't' "))
    xx = math.ceil(math.pow(x,2))
    # equaçao de cima
    aa = (a)*xx
    bb = (b)*(x)
    res = ((aa) + (bb))
    #equaçao de baixo
    aa2 = a2*xx
    bb2 = b2*x
    res2 = ((aa2)+(bb2)+(c2))

    print(f"\nlim     {a}x² + {b}x               {a}.{x}² + {b}.{x}                {aa} + {bb}                     {res}     ")
    print(f"X→{x}  -------------------- =    --------------------- =    ----------------------- =    --------------")
    print(f"       {a2}x² + {b2}x {c2}               {a2}{x}² + {b2}x {c2}                 {aa2} + {bb2} + {c2}            {res2}\n\n")

    if res == 0 and res2 == 0:
        in_x = x*(-1)
        abss_a = abs(a)
        abss_b = abs(b)
        if abss_a < abss_b:
            n = a
        else:
            n = b
        nn = (n)*(x)
        div = (c2)/in_x
        soma2 = math.ceil((x) + (div))
        print(f"\nlim     {a}x² + {b}                lim  (x | {in_x}).({n}.x)                {n} . {x}                      {nn}     ")
        print(f"X→{x}  -------------------- =    x→{in_x} ---|----------------- =    ----------------------- =    --------------")
        print(f"         x² + {b2}x + {c2}            (x | {in_x}).(x + {div})           {x} + {div}                     {soma2}\n\n")
    elif res !=0 and res2 !=0:
        None
    else:
        print("não ha solução disponivel no momento")
