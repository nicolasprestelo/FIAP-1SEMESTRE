def lista_caracteres(lista, n):
    nomes_maiores = []

    for nome in lista:
        if len(nome) > n:
            nomes_maiores.append(nome)
    return nomes_maiores

nomes = ["Nicolas", "Pedro", "Lucas", "Rodrigo", "João"]

n_caracteres = int(input("Digite o número de caracteres: "))

resultado = lista_caracteres(nomes, n_caracteres)
print(resultado)