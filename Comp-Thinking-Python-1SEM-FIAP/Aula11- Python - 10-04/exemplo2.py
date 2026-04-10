print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Escolha uma das opções acima: "))

if 1 <= opcao <= 4 :
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))

match opcao:
    case 1:
        print(f"Resultado da Soma {a + b}")
    case 2:
        print(f"Resultado da Subtração {a - b}")
    case 3:
        print(f"Resultado da Multiplicação {a * b}")
    case 4:
        if b == 0:
            print("ERRO: Não é possível dividir por zero.")
        else:
            print(f"Resultado da Divisão {a / b}")
    case _:
        print("Opção inválida.")