#importa a biblioteca Sympy
from sympy import *
init_printing()
#define x e y como variáveis simbólicas.
x, y = symbols('x y')
#define a função f(x)
def f(x): return (x**3 - 3*x + 2)*exp(-x/4) - 1
#mostra a função f(x)
f(x)
f(1)
f(x-2)
def g(x): return 2 - sqrt(x**2 - 1)
f(x)