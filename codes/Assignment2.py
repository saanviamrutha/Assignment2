import sympy as smp
x = smp.symbols('x')
f = (x)*(1+x**2)/(1+x**4)
s = smp.integrate(f,x)
print(s)
