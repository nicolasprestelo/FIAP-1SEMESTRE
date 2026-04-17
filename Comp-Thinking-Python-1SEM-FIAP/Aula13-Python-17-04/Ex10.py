voto1 = 0
voto2 = 0
voto3 = 0
votoBranco = 0

while True:

    print("\n 1 - Candidato 1")
    print(" 2 - Candidato 2")
    print(" 3 - Candidato 3")
    print(" 4 - Voto em Branco")
    print(" 5 - Finalizar")
    voto = int(input(" Informe o seu voto: "))

    match voto:
        case 1:
            voto1 += 1
            print(f"Voto no candidato 1 computado com sucesso.")
        case 2:
            voto2 += 1
            print(f"Voto no candidato 2 computado com sucesso.")
        case 3:
            voto3 += 1
            print(f"Voto no candidato 3 computado com sucesso.")
        case 4:
            votoBranco += 1
            print(f"Voto em Branco computado com sucesso.")
        case 5:
            print("Finalizando a eleição.\n")
            break

totalVotos = voto1 + voto2 + voto3 + votoBranco

print(f"Votos:\nCandidato 1: {voto1} votos\nCandidato 2: {voto2} votos\nCandidato 3: {voto3} votos"
      f"\nVotos em Branco: {votoBranco}\nO percentual de Votos Brancos foi de {(votoBranco / totalVotos) * 100:.2f}%")

if voto1 > voto2 and voto1 > voto3:
    candidatoVencedor = "Candidato 1"
    print(f"O Vencedor da eleição foi o {candidatoVencedor}")

elif voto2 > voto1 and voto2 > voto3:
    candidatoVencedor = "Candidato 2"
    print(f"O Vencedor da eleição foi o {candidatoVencedor}")

elif voto3 > voto1 and voto3 > voto2:
    candidatoVencedor = "Candidato 2"
    print(f"O Vencedor da eleição foi o {candidatoVencedor}")

else:
    print("Houve um empate, a eleição deve ocorrer novamente.")
