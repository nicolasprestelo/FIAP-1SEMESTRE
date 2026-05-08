import random
from random import randint

lista = []
somatorio = 0
maior_numero = 0
menor_numero = 50

while len(lista) != 20:
    numero = random.randint(1, 50)
    lista.append(numero)
    somatorio += numero
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print(f"Lista dos números sorteados: {lista}")
print(f"Somatório dos números contidos: {somatorio}")
print(f"Maior número sorteado: {maior_numero}")
print(f"Menor número sorteado: {menor_numero}")