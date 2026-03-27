numero = int(input("Digite um número inteiro: "))

if numero < 0:
    numero = numero * -1
    print(f"O seu número em forma positiva é {numero}")

print(f"O seu número é {numero}")