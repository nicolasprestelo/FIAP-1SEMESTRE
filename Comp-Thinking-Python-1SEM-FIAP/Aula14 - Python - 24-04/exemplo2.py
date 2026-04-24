# Solicitar 10 números e contar qunatos numeros são pares
# e quantos números são ímpares

cont_pares = 0
cont_impares = 0

for cont in range(10):
    numero = int(input("Número: "))
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

print(f"Quantidade de números pares: {cont_pares}")
print(f"Quantidade de números pares: {cont_impares}")
