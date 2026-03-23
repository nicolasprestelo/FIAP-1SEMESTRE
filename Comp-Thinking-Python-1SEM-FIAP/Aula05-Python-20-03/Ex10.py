import math

#Receber as dimensões

comprimento = float(input("Digite o comprimento da cozinha: "))
largura = float(input("Digite a largura da cozinha: "))
altura = float(input("Digite a altura da cozinha: "))


#Caixa cobre 1.5m²

areaParede1 = largura * altura
areaParede2 = comprimento * altura

areaTotal = (areaParede2 * 2) + (areaParede1 * 2)
quantidadeAzulejos = areaTotal / 1.5
quantidadeAzulejos = math.ceil(quantidadeAzulejos)

print(f"Para revestir a  será necessario {quantidadeAzulejos} azulejos")