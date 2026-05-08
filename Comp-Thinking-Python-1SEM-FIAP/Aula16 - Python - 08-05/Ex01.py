lista_pares = []
lista_impares = []

for i in range(10):
    numero = int(input("Informe um número: "))

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append((numero))

print(f"Números pares armazenados: {lista_pares}")
print(f"Números impares armazenados: {lista_impares}")