# ex30_4.py
import sympy as sp

x = sp.Symbol('x')
f1 = -x**2 + 2*x
print("f1'(x) = ", sp.integrate(f1, x))
f2 = sp.E**x
print("f2'(x) = ", sp.integrate(f2, x))
f3 = sp.log(x)
print("f3'(x) = ", sp.integrate(f3, x))


















