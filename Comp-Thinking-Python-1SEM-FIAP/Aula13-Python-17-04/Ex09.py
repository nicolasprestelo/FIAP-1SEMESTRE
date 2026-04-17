saldo = 0.00
opcao = 0

def menu():
    print(" 1 - Consultar Saldo")
    print(" 2 - Realizar Saque")
    print(" 3 - Realizar depósito")
    print(" 4 - Sair")
    opcao = int(input(" Escolha uma opção: "))
    return opcao


while True:

    print("\n 1 - Consultar Saldo")
    print(" 2 - Realizar Saque")
    print(" 3 - Realizar depósito")
    print(" 4 - Sair")
    opcao = int(input(" Escolha uma opção: "))

    match opcao:
        case 1:
            print(f"O seu saldo é de R${saldo:.2f}")
        case 2:
            saque = float(input(f"Digite o valor do saque: "))
            if saque > saldo:
                print("Não foi possível realizar o saque, pois o saldo é inferior ao valor de retirada.")
            else:
                saldo -= saque
                print(f"Saque de R${saque:.2f} realizado com sucesso.")
        case 3:
            deposito = float(input("Digite o valor do depósito: "))
            saldo += deposito
            print(f"Depósito de R${deposito:.2f} realizado com sucesso.")
        case 4:
            print("Saindo...")
            break