# ex30_2.py
import sympy as sp

x, y = sp.symbols(('x','y'))
eq1 = 2*x + y - 1 
eq2 = x - 2*y
ans = sp.solve((eq1,eq2))
print(ans)















