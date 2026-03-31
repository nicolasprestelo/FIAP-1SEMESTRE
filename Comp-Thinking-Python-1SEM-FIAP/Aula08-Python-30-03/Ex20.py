print("Bem-vindo a nossa lanchonete!!")
print("Cardápio:\n")
print("Nome --- Código --- Preço (R$)")
print("Cachorro Quente --- 100 --- 13.20")
print("Hambúrguer --- 101 --- 19.20")
print("Cheeseburquer --- 102 --- 21.20")
print("Suco Natural --- 103 --- 7.00")
print("Refrigerante --- 104 --- 6.50\n")

codigo = int(input("Digite o código do produto escolhido: "))
quantidade = int(input("Digite a quantidade do produto: "))

if codigo == 100:
    preco = quantidade * 13.2
    print(f"O valor a ser pago será de R${preco}")
elif codigo == 101:
    preco = quantidade * 19.2
    print(f"O valor a ser pago será de R${preco}")
elif codigo == 102:
    preco = quantidade * 21.2
    print(f"O valor a ser pago será de R${preco}")
elif codigo == 103:
    preco = quantidade * 7
    print(f"O valor a ser pago será de R${preco}")
elif codigo == 104:
    preco = quantidade * 6.5
    print(f"O valor a ser pago será de R${preco}")


