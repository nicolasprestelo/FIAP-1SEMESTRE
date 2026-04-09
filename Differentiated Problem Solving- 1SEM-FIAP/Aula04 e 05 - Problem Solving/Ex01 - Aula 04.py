import sympy

from sympy import symbols, simplify

# Definir as variáveis
x, y, z, a, b, c = symbols("x y z a b c")

# a)

expr1_a = (3 * x + 2 * y - 5) + (4 * x - y + 8)
print(simplify(expr1_a))

expr1_b = (5 * x ** 2 - x + 1) - (2 * x ** 2 + 4 * x - 3)
print(expr1_b)

expr1_c = 7 * z ** 2 - (3 * z ** 2 - 5 * z ** 2 + 1)
print(expr1_c)

expr1_d = (6 * a ** 2 - 3 * b) - (2 * a ** 2 + 5 * b - 7)
print(expr1_d)

expr1_e =  (-2 * a + 5 * b - 3 * c) + (7 * a - b + 2 * c)
print(expr1_e)
