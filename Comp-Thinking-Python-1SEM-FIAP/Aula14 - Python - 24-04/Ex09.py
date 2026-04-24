numero = int(input("Número: "))
fatorial = 1

for i in range(numero, 1, -1):
    fatorial *= i

print(f"O fatorial do número {numero} é {fatorial}")