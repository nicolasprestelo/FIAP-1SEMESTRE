numero = int(input("Digite um número: "))

print("1 - O dobro")
print("2 - A metade")
print("3 - 10% do número")
opcao = int(input("Escolha uma das opções acima: "))

match opcao:
    case 1:
        print(f"O dobro do número é {numero * 2}")
    case 2:
        print(f"A metade do número é {numero / 2}")
    case 3:
        print(f"10% do número é {numero * 0.1}")
    case _:
        print("Opção inválida")