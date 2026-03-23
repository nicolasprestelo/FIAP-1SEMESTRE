votosBrancos = int(input("Digite a quantidade de votos brancos: "))
votosNulos = int(input("Digite a quantidade de votos nulos: "))
votosValidos = int(input("Digite a quantidade de votos validos: "))

totalDeVotos = votosValidos + votosNulos + votosBrancos
print(f"Do total de {totalDeVotos} votos, {(votosBrancos/totalDeVotos)*100:.2f}% são brancos, {(votosNulos/totalDeVotos) * 100:.2f}% são nulos e {(votosValidos/totalDeVotos) * 100:.2f}% são votos válidos")