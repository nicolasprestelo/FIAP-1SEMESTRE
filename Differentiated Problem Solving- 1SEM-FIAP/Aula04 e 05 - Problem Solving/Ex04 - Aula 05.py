import sympy

from sympy import symbols, Eq, solve

x = symbols("x")

eq04_a = Eq(x ** 2 - 6 * x + 7, 0)
resultado_a = solve(eq04_a, x)
print(resultado_a)

eq04_b = Eq(x ** 2 + 3 * x - 28, 0)
resultado_b = solve(eq04_b, x)
print(resultado_b)

eq04_c = Eq(4 * x ** 2 - 12 * x + 7, 0)
resultado_c = solve(eq04_c, x)
print(resultado_c)

eq04_d = Eq(x ** 2 + 8 * x + 16 , 0)
resultado_d = solve(eq04_d, x)
print(resultado_d)