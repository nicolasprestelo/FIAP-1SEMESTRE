individuos = int(input("Digite o número de individuos: "))
cont = 1
soma = 0

while cont < individuos:
    if cont == individuos:
        idade = 0
        soma += idade
        cont += 1
    else:
        idade = int(input("Digite a idade: "))
        soma += idade
        cont += 1

media = soma / individuos
print(f"A média das idades desses {individuos} individuos é de {media}")