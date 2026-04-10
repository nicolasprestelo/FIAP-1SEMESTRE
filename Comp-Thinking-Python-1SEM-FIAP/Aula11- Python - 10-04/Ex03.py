numero = int(input("Digite um número inteiro: "))

match numero % 3:
    case 0:
        print("O número é múltiplo de 3")
    case _:
        print("O número NÃO é múltiplo de 3.")