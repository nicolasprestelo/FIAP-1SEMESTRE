import sympy

from sympy import symbols, simplify

#Definir variáveis

x, y, a, b = symbols("x y a b")

expr2_a = (-8 * x ** 3) *  (4 * x)
print(expr2_a)

expr2_b =  5 * a ** 4 * x ** 3 * 2 * a * x ** 4
print(expr2_b)

expr2_c = 12 * y ** 5 / 4 * y ** 3
print(expr2_c)

expr2_d = 20 * a ** 4 * b ** 2 / (-5 * a * b)
print(expr2_d)

expr2_e =  (3 * x ** 2 * y) * (2 * x ** 3)
print(expr2_e)