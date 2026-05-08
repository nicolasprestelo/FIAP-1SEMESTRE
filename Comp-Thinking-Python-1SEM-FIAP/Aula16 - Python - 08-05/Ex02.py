from plotly.data import medals_long

lista = []
somatorio_pares = 0
media = 0
for i in range(10):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        somatorio_pares += numero
    media += numero
    lista.append(numero)
media = media / 10
print(f"A média aritimética dos números foi de {media:.2f}")
print(f"O somatório de números pares foi de {somatorio_pares}")