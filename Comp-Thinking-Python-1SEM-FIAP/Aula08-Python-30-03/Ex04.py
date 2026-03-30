numero = int(input("Digite um número entre 0 e 1000: "))

centena = numero // 100 #251 = 2
unidade = numero % 10 #251 = 1
dezena =  (numero % 100) // 10 #251 = 5

soma = centena + unidade + dezena
print(f"A soma dos algarismos é {soma}")