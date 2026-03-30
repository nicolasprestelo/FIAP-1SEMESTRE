numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f"O maior número é {numero1}, já a diferença entre eles é {diferenca} ")

elif numero2 > numero1:
    diferenca = numero2 - numero1
    print(f"O maior número é {numero1}, já a diferença entre eles é {diferenca} ")
else:
    print("Os número são iguais, sua diferença é zero (0)")