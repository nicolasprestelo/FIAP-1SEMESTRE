valor_x = float(input("Digite o valor de X: "))

if valor_x <= 1:
    valor_x = 1
    print(f"O valor de f(x) é {valor_x}")
elif valor_x <= 2:
    valor_x = 2
    print(f"O valor de f(x) é {valor_x}")
elif valor_x <= 3:
    valor_x = valor_x ** 2
    print(f"O valor de f(x) é {valor_x}")
else:
    valor_x = valor_x ** 3
    print(f"O valor de f(x) é {valor_x}")