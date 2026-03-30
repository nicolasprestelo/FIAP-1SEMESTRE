numero1 = int(input("Digite um número inteiro: "))

if numero1 % 3 == 0 and numero1 % 5 == 0:
    print("O número não passou na verificação, pois é divisivel simutaneamente por 3 e 5.")
elif numero1 % 3 == 0 or numero1 % 5 == 0:
    print("O número passou na verificação.")
else:
    print("O número não passou na verificação")