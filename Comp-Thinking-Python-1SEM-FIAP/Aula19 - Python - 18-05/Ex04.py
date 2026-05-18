def alterar_lista(lista, media_lista):

    lista_alterada = []
    for i in range(len(lista)):
        if lista[i] > media_lista:
            lista_alterada.append(lista[i])
    return lista_alterada

entrada = input("Digite os números da lista, separados por espaço: ")
lista_usuario = [int(numero) for numero in entrada.split()]
media_lista = 0
for i in range(len(lista_usuario)):
    media_lista += lista_usuario[i]

media_lista = media_lista / len(lista_usuario)

print(alterar_lista(lista_usuario, media_lista))