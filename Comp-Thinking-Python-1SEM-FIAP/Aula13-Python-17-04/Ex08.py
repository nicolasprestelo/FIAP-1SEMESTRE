numero = -1
multiplicacao = 1
soma = 0

while numero != 0:
    numero = int(input("Digite números para realizar a multiplicação (0 para sair): "))
    if numero % 2 == 0:
        soma += numero
    else:
        multiplicacao *= numero
print(f"Soma dos números pares: {soma}\nMultiplicação dos números ímpares: {multiplicacao}")
