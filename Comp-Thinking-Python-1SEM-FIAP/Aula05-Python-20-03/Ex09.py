diasTrabalhados = int(input("Digite a quantidade de dias trabalhados: "))
valorSemDesconto = diasTrabalhados * 180
valorFinal = valorSemDesconto * .92

print(f"O funcionário receberá {valorFinal}R$")