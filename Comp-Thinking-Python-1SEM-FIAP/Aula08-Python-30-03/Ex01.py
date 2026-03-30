numero = int(input("Digite um número: "))

if numero >= 0:
    numero = numero / 2
    print(f"O seu número é {numero}")
else:
    numero = numero**2
    print(f"O seu número é {numero}")