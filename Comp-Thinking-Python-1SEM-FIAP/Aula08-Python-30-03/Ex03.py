nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"A média do aluno é de {media}")
else:
    print("As notas apresentadas não são válidas. Digite valores entre 0 e 10.")