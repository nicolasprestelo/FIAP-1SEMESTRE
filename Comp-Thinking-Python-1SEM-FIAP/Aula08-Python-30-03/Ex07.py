nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3 * 2) / 4

if media >= 6:
    print(f"O aluno foi aprovado com média {media}.")
else:
    print(f"O aluno foi repovado com média {media}.")