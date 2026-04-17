numero = int(input("Digite um número positivo: "))
cont = 1
numero_perfeito = 0

while cont != numero:
    if numero % cont == 0:
        numero_perfeito += cont
        cont += 1
    else:
        cont += 1
if numero_perfeito == numero:
    print(f"O número {numero} é perfeito.")
else:
    print("O número não é perfeito.")