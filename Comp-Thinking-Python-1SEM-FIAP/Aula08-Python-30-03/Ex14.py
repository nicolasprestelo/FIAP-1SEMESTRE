valor_a = float(input("Digite o valor A: "))
valor_b = float(input("Digite o valor B: "))
valor_c = float(input("Digite o valor C: "))

if valor_a >= valor_b and valor_b >= valor_c:
    print("Os valores estão em ordem decrescente.")
elif valor_c >= valor_b and valor_b >= valor_a:
    print("Os valores estão em ordem crescente.")
else:
    print("Os valores estão desordenados.")