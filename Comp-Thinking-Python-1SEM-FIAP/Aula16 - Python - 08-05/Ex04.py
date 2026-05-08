lista_nome = []
lista_idade = []

for i in range(10):
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    lista_nome.append(nome)
    lista_idade.append(idade)

for i in range(len(lista_idade)):
        if lista_idade[i] >= 18:
            print(f"{lista_nome[i]} é maior de idade, possui {lista_idade[i]} anos")
