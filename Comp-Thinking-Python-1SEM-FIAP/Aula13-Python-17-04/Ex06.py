numero = int(input("Digite um número inteiro: "))
cont = 1
verificar_primo = 0

while cont <= numero:
    if numero % cont == 0:
        verificar_primo += cont
        cont += 1
    else:
        cont += 1
if verificar_primo == 1 + numero:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")