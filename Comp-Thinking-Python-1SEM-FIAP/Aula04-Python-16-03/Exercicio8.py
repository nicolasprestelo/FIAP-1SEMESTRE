

nome = input("Nome do vendedor: ")
quantidadeCarrosVendidos = int(input("Quantidade de carros vendidos: "))
valorTotal = float(input("Valor total das vendas: "))

salarioBase = 2500
salarioComissao = 200 * quantidadeCarrosVendidos + (0.02 * valorTotal)
salarioTotal = salarioBase + salarioComissao

print(f"O salário do vendedor {nome} é de {salarioTotal}")

