def menu_inicial():
    while True:
        print("Calculadora:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair do programa")
        opcao_escolhida = int(input("Selecione a sua opção: "))

        if opcao_escolhida == 5:
            print("Saindo...")
            break

        numero1 = int(input("Informe o primeiro número: "))
        numero2 = int(input("Informe o primeiro número: "))
        match opcao_escolhida:
            case 1:
                print(f"O resultado foi de {adicao(numero1, numero2)}")
            case 2:
                print(f"O resultado foi de {subtracao(numero1, numero2)}")
            case 3:
                print(f"O resultado foi de {multiplicacao(numero1, numero2):.2f}")
            case 4:
                print(f"O resultado foi de {divisao(numero1, numero2):.2f}")
            case _:
                print("Valor inválido! Insira outro valor")

def adicao(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 / numero2

menu_inicial()
