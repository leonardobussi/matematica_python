a = int(input("digite a: "))
b = int(input("digite b: "))
if (a != 0):
    print("fx = aX + b")
    print("fx = {0} + {1}".format(a,b))
    if (b != 0):
        b = b * (-1)
        x = b/a
        print("x = {0}/{1}".format(b,a))
        print("x = ", x)
    else:
        print("x = {0}/{1}".format(b,a))
        print("x = 0")
else:
    print("impossivel resolver")
