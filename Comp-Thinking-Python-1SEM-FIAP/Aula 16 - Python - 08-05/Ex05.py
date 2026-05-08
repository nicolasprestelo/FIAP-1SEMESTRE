import random

lista = []
contador = 0
for i in range(10):
    numero = random.randint(1, 10)
    lista.append(numero)

numero_usuario = int(input("Digite um número de 1 a 10: "))

for i in range(len(lista)):
    if numero_usuario == lista[i]:
        contador += 1
print(f"O seu número aparece na lista {contador} vezes")
print(lista)