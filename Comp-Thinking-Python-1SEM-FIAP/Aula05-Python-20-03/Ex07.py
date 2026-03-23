custoFabrica = float(input("Digite o custo de fábrica para a fabricação do carro: "))
percentualDistrubuidor = custoFabrica * .28
impostos = custoFabrica * .45
valorTotal =  custoFabrica + percentualDistrubuidor + impostos

print(f"O valor total do carro ao consumidor é de {valorTotal:.2f}R$")