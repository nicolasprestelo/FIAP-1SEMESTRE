import sympy

from sympy import symbols, Eq, solve

x = symbols("x")

eq03_a =  Eq(6 * x, 2 * x + 16)
resultado_a = solve(eq03_a, x)
print(resultado_a)

eq03_b = Eq(2 * x - 5,  x + 1)
resultado_b = solve(eq03_b, x)
print(resultado_b)

eq03_c = Eq(2 * x + 3, x + 4)
resultado_c = solve(eq03_c, x)
print(resultado_c)

eq03_d = Eq(5 * x + 7, 4 * x + 10)
resultado_d = solve(eq03_d, x)
print(resultado_d)
