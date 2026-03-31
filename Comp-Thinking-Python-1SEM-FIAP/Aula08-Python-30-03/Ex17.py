from traceback import print_tb

valor_pruduto = float(input("Digite o valor do produto: "))
estado = input("Digite o estado de destino do produto: ")
if estado.upper() == "SP":
    imposto = valor_pruduto * 0.12
    print(f"O valor final do seu produto será de R${valor_pruduto + imposto}.")
elif estado.upper() == "MG":
    imposto = valor_pruduto * 0.07
    print(f"O valor final do seu produto será de R${valor_pruduto + imposto}.")
elif estado.upper() == "RJ":
    imposto = valor_pruduto * 0.15
    print(f"O valor final do seu produto será de R${valor_pruduto + imposto}.")
elif estado.upper() == "MS":
    imposto = valor_pruduto * 0.08
    print(f"O valor final do seu produto será de R${valor_pruduto + imposto}.")
else:
    print("Digite um estado válido. (SP/MG/RJ/MS)")