numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
numero3 = float(input("Digite outro número novamente: "))

if numero1 > numero2 and numero3 > numero2:
    print(f"O menor número é {numero2}")
elif numero2 > numero1 and numero3 >numero1:
    print(f"O menor número é {numero1}")
elif numero1 == numero2 and numero3 == numero1:
    print("Os números são iguais")
else:
    print(f"O menor número é {numero3}")