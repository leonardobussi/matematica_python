
import random
l = [1,0]
a00 = random.choice(l)
a01 = random.choice(l)
a02 = random.choice(l)
a03 = random.choice(l)
a10 = random.choice(l)
a11 = random.choice(l)
a12 = random.choice(l)
a13 = random.choice(l)
a20 = random.choice(l)
a21 = random.choice(l)
a22 = random.choice(l)
a23 = random.choice(l)
a30 = random.choice(l)
a31 = random.choice(l)
a32 = random.choice(l)
a33 = random.choice(l)
a = a00, a01
b = a00, a10
c = a01, a11
d = a10, a11 
print()
print("matriz 2×2")
print()
print("[ {0}  {1} ]\n[ {2}  {3} ]".format(a00,a01,a10,a11))
print()
if (a == b) or (a == c) or (b == d) or (c == d):
    print("essa matriz e simetrica")
else:
    print("nao eh simetrica")
print()
#########################################################################################
print()
print("matriz 3×3")
a = a00, a01, a02
b = a00, a10, a20
c = a02, a12, a22
d = a20, a21, a22
print()
print("[ {0}  {1}  {2} ]\n[ {3}  {4}  {5} ]\n[ {6}  {7}  {8} ]".format(a00,a01,a02,a10,a11,a12,a20,a21,a22))
print()
if (a == b) or (a == c) or (b == d) or (c == d):
    print("essa matriz e simetrica")
else:
    print("nao eh simetrica") 
####################################################################
print()
print("matriz 4×4")
a = a00, a01, a02, a03
b = a00, a10, a20, a30
c = a03, a13, a23, a33
d = a30, a31, a32, a33
print()
print("[ {0}  {1}  {2}  {3} ]\n[ {4}  {5}  {6}  {7} ]\n[ {8}  {9}  {10}  {11} ]\n[ {12}  {13}  {14}  {15} ]".format(a00,a01,a02,a03,a10,a11,a12,a13,a20,a21,a22,a23,a30,a31,a32,a33))
print()
if (a == b) or (a == c) or (b == d) or (c == d):
    print("essa matriz e simetrica")
else:
    print("nao eh simetrica") 