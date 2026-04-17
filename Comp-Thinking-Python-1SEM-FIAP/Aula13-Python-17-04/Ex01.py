n = int(input("Digite um número: "))
cont = 0

while cont < n:
    if cont % 2 == 0:
        cont += 1
    else:
        print(f"Número ímpar: {cont}")
        cont += 1