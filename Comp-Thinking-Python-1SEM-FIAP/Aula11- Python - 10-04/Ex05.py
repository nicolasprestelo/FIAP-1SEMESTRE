print("1 - Picanha - R$25,00")
print("2 - Lasanha - R$20,00")
print("3 - Strogonoff - R$20,00")
print("4 - Bife acebolado - R$15,00")
print("5 - Pão com Ovo - R$5,00")
opcao = int(input("Escolha o código referente ao prato desejado: "))

match opcao:
    case 1:
        valor_prato = 25
        print("Maravilha, logo traremos o seu pedido!!")
    case 2:
        valor_prato = 20
        print("Maravilha, logo traremos o seu pedido!!")
    case 3:
        valor_prato = 20
        print("Maravilha, logo traremos o seu pedido!!")
    case 4:
        valor_prato = 15
        print("Maravilha, logo traremos o seu pedido!!")
    case 5:
        valor_prato = 5
        print("Maravilha, logo traremos o seu pedido!!")
    case _:
        print("Opção inválida.")

taxa = input("Você aceita pagar uma taxa de serviço de 10%? (S/N):  ").upper()
match taxa:
    case "S":
        print(f"Muito obrigado! A sua conta total ficou no valor de R${ valor_prato + (valor_prato * 0.10)}")
    case "N":
        print(f"Certo, o valor do prato ficou em R${valor_prato} ")
    case _:
        print("Opção inválida.")