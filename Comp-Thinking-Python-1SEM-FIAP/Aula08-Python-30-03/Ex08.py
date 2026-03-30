nota1 = float(input("Digite sua nota no Trabalho do Laboratório (0 a 10): "))
nota2 = float(input("Digite sua nota na Avaliação Semestral (0 a 10): "))
nota3 = float(input("Digite sua nota no Exame Final(0 a 10): "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

if media >= 6:
    print(f"O aluno foi aprovado com média {media}.")
else:
    print(f"O aluno foi repovado com média {media}.")

