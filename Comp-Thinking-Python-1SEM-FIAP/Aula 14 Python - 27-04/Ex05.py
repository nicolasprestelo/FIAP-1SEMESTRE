import random

tentativas = 1
numero_secreto = random.randint(1, 100)
resposta = 0

while resposta != numero_secreto:
    resposta = int(input("\nTente adivinhar o número secreto de 1 a 100!\nResposta: "))
    if resposta > numero_secreto:
        print("Resposta errada!")
        print(f"O número secreto é menor que {resposta}\nTente Novamente")
        tentativas += 1
    elif resposta == numero_secreto:
        print(f"Você acertou!! O número secreto era {numero_secreto}")
        print(f"O número de tentativas foi {tentativas}")
    else:
        print("Resposta errada!")
        print(f"O número secreto é maior que {resposta}\nTente Novamente")
        tentativas += 1

