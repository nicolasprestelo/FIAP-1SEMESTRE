import random

senha_1 = random.randint(0, 9)
senha_2 = random.randint(0, 9)
senha_3 = random.randint(0, 9)

verificar_senha1 = 0
verificar_senha2 = 0
verificar_senha3 = 0
tentativas = 0

while verificar_senha1 != senha_1:
    verificar_senha1 += 1
    tentativas += 1

while verificar_senha2 != senha_2:
    verificar_senha2 += 1
    tentativas += 1

while verificar_senha3 != senha_3:
    verificar_senha3 += 1
    tentativas += 1

print(f"Senha encontrada: {senha_1}{senha_2}{senha_3}")
print(f"Tentativas realizadas: {tentativas}")


