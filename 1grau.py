print ("\n \n f(x) = ax + b \n")
print ("\n Digite os valores para: \n")

a = int(input("a: "))
b = int(input("b: "))

raiz = -b/a

if (a == 0):
   print ("\n\n Não é uma função do primeiro grau ")
elif (a>0):
   print("\n\n Função de primeiro grau crecente\n" )
   print("\nRaiz da equação: ",raiz)
   print("\n Par ordenado: (x,y) = ("+str(raiz)+",0)") 
   print("\nIntercepto em y: ",b)
   print("\nPar ordenado (x,y) = (0,"+str(b)+")")
else:
   print("\n\n Função de primeiro grau decrescente\n" )
   print("\nRaiz da equação: ",raiz)
   print("\n Par ordenado: (x,y) = ("+str(raiz)+",0)") 
   print("\nIntercepto em y: ",b)
   print("\nPar ordenado (x,y) = (0,"+str(b)+")")

