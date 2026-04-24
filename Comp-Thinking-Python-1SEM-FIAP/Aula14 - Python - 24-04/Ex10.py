quantidade_alunos = int(input("Digite a quantidade de alunos: "))
quantidade_notas = int(input("Digite a quantidade de notas: "))
soma_notas = 0

for i in range(quantidade_alunos):

    for nota in range(quantidade_notas):
        notas = float(input(f"Digite as notas do {i + 1}° aluno: "))
        soma_notas += notas

    media = soma_notas / quantidade_notas

    print(f"\nMédia do {i + 1}° aluno: {media:.2f}")
    soma_notas = 0
    media = 0