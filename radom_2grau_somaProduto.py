import random

a = int(input("\ndigite o a: "))
b = int(input("digite o b: "))
c = int(input("digite o c: "))
b = b * (-1)
print(f"\n{a}X² + {b}X + {c} = 0\n ")
contador = 1
while contador <= 100:
 
    numero1 = random.choice([0]) #n1
    numero2 = random.choice([0]) #n2
    soma = numero1 + numero2 # rs = (n1) + (n2)
    multiplicacao = numero1 * numero2 # rp  = (n1) + n2

    while soma != b and multiplicacao != c:    #rs != (b) and rp != (c):
        numero1 = random.choice([-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) #n1
        numero2 = random.choice([-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])  #n2
        soma = numero1 + numero2  #rs = (n1) + (n2)
        multiplicacao = numero1 * numero2  #rp = (n1) * (n2)

    else:
        if soma == b and multiplicacao == c: #(rs == (b)) and (rp == (c)):
            print(f"{numero1} + {numero2} = {b} ")
            print(f"{numero1} × {numero2} = {c} ")
            print(f"as raizes sao:  {numero1} e {numero2} ")
            break
    contador += 1
    if contador == 100:
        print("expressao incorreta")
        break        