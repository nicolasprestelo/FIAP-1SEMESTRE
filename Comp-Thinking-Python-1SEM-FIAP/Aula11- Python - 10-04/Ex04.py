print("1 - Linux")
print("2 - Banco de Dados")
print("3 - Windows Server")
print("4 - Lógica e Programação")

codigo_palestra = int(input("Digite o código da palestra: "))

match codigo_palestra:
    case 1:
        print("A palestra será realizada no Auditório 1")
    case 2:
        print("A palestra será realizada no Auditório 2")
    case 3:
        print("A palestra será realizada no Auditório 3")
    case 4:
        print("A palestra será realizada no Auditório Principal")
    case _:
        print("Nenhuma palestra localizada nesse código.")