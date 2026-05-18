def buscar_indices(lista, valor_busca):
    return [indice for indice, item in enumerate(lista) if item == valor_busca]

entrada = input("Digite os números da lista, separados por espaço: ")

lista_usuario = [int(numero) for numero in entrada.split()]

busca = int(input("Qual valor que você quer buscar: "))

resultado = buscar_indices(lista_usuario, busca)
print(f"O número {busca} foi encontrado nas posições: {resultado}")