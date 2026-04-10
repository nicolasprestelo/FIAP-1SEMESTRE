
valor = float(input("Digite o valor a ser pago: "))
tipo_cliente = input("Você a sua clientela. Cliente Comum (C), Funcionário (F) ou Vip (V): ").upper()

match tipo_cliente:
    case "C":
        print(f"Para cliente Comum infelizmente não há desconto. O valor é de {valor}")

    case "F":
        desconto = valor * 0.1
        valor = valor - desconto
        print(f"Funcionários tem 10% de desconto!\nO valor final já com esse beneficio é de {valor}")

    case "V":
        desconto = valor * 0.05
        valor = valor - desconto
        print(f"Vips tem 5% de desconto!\nO valor final já com esse beneficio é de {valor}")
    case _:
        print("Tipo de cliente não encontrado.")