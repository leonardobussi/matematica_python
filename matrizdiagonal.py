a00 = int(input("digite a posiçao 00: ")) #principal -1-
a01 = int(input("digite a posiçao 01: ")) 
a02 = int(input("digite a posiçao 02: ")) #secundaria -1-
a10 = int(input("digite a posiçao 10: ")) 
a11 = int(input("digite a posiçao 11: ")) #principal e secundaria -2-
a12 = int(input("digite a posiçao 12: ")) 
a20 = int(input("digite a posiçao 20: ")) #secundaria -3-
a21 = int(input("digite a posiçao 21: ")) 
a22 = int(input("digite a posiçao 22: ")) #principal -3-
print()
print("[[    {0}    {1}    {2}    ]]\n[[    {3}    {4}    {5}    ]]\n[[    {6}    {7}    {8}    ]] ".format(a00,a01,a02,a10,a11,a12,a20,a21,a22))
print()
matriz = a00 * a11 * a22
matriz1 = a02 * a11 * a20
print("a diagonal principal eh 00 × 11 × 22 e o resultado deu: {0}".format(matriz))
print("diagonal segundaria eh 02 × 11 × 20 e o resultado deu: {0}".format(matriz1))
total = (matriz) - (matriz1)
print("e o resultado deu", total)