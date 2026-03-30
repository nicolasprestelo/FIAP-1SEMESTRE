numero = int(input("Digite um número entre 0 e 1000: "))

centena = numero // 100 #251 = 2
unidade = numero % 10 #251 = 1

if centena == unidade:
    print(f"Esse número é capicua")
else:
    print("Esse número não é capicua")