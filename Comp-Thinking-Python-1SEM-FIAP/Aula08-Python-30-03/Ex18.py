distancia = float(input("Digite a quantidade de Km percorrido: "))
quantidade_gasolina = float(input("Digite a quantidade de gasolina utilizada: "))

consumo = distancia / quantidade_gasolina

if consumo < 8:
    print("Venda o carro.")
elif 14 >= consumo > 8:
    print("Econômico.")
elif consumo > 14:
    print("Supereconômico.")
else:
    print("Consumo não se adequa á tabela.")