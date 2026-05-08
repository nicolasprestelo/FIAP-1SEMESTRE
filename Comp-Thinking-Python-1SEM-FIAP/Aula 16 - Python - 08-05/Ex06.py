lista_notas = []
media = 0
contador_notas_acima_media = 0
while True:
    notas_alunos = int(input("Informe a nota dos alunos (Digite -1 para sair): "))
    if notas_alunos < 0:
        break
    else:
        lista_notas.append(notas_alunos)
        media += notas_alunos

calculo_media = media / len(lista_notas)
print(f"A quantidade de notas informadas foi de {len(lista_notas)}")
print(f"Notas: {lista_notas}")
print(f"A média das notas foi de {calculo_media:.2f}")

for i in range(len(lista_notas)):
    if lista_notas[i] > calculo_media:
        contador_notas_acima_media += 1

print(f"A quantidade de notas acima da média foi de {contador_notas_acima_media}")