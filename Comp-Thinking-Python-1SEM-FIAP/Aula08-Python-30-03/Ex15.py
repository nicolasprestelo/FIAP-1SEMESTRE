idade = int(input("Digite a sua idade: "))
tempo_servico = int(input("Digite o seu tempo de serviço: "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("A pessoa tem condições de aposentadoria.")
else:
    print("A pessoa NÃO tem condições de aposentadoria.")