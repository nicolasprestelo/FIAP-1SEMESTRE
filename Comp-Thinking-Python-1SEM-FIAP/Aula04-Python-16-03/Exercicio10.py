numeroPedido = int(input("Digite um número inteiro com três dígitos: "))

unidade = numeroPedido % 10
# Pega o resto da divisão por 10
# ex: 123 / 10 =  12.3 ---> 12 dezenas inteiras com resto 3
# logo o valor é o resto, 3

dezena = (numeroPedido // 10 ) % 10
#Pega o resultado inteiro da divisao por 10 e pega o resto da divisao por 10 dnv
# Ex: 123 // 10 =  12 INTEIROS, 12 / 10 = 1.2 ---> 1 dezena inteira com resto 2
# logo o valor é o resto, 2

centena = numeroPedido // 100
#Divide o número por 100, pega o resultado inteiro
#Ex: 123 // 100 = 1
#logo, valor = 1


numeroInvertido = unidade * 100 + dezena * 10 + centena
print(f"Número invertido: {numeroInvertido}")
