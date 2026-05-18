def filtrar_intervalo(lista, min, max):
    lista_intervalo = []
    for i in range(len(lista)):
        if lista[i] > min and lista[i] < max:
            lista_intervalo.append(lista[i])

    return lista_intervalo



lista_numeros = [1, 2, 3, 4, 6, 9, 10, 20, 5, 6, 2]
minimo = int(input("Digite o intervalo minimo: "))
maximo = int(input("Digite o intervalo maximo: "))
print(filtrar_intervalo(lista_numeros, minimo, maximo))