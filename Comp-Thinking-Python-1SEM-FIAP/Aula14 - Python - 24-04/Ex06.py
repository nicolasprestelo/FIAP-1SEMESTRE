menor = int(input("Número: "))
maior = menor

for numero in range(9):
    numero = int(input("Número: "))

    if numero < menor:
        menor = numero

    if numero > maior:
        maior = numero

print(f"O maior número foi {maior}")
print(f"O menor número foi {menor}")