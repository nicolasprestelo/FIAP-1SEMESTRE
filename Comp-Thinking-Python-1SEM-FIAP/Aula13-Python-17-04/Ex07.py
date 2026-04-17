numero_entrada = int(input("Digite um número inteiro positivo: "))
soma = 0

while numero_entrada > 0:
    resto = numero_entrada % 10   #1234 = 4  --- = 3
    numero_entrada = numero_entrada //  10  #1234 = 123 --- = 12
    soma += resto  # = 4

print(f"A soma dos algarismos é {soma}")