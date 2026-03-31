from traceback import print_tb

numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
numero3 = float(input("Digite o terceiro valor: "))

if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(f"{numero3} e {numero2} e {numero1}")
    elif numero3 > numero2:
        print(f"{numero2} e {numero3} e {numero1}")
    else:
        print(f"{numero3} e {numero2} e {numero1}")

elif numero2 > numero1 and numero2 > numero3:
    if numero3 > numero1:
        print(f"{numero1} e {numero3} e {numero2}")
    elif numero1 > numero3:
        print(f"{numero3} e {numero1} e {numero2}")
    else:
        print(f"{numero3} e {numero1} e {numero2}")

elif numero3 > numero1 and numero3 > numero2:
    if numero2 > numero1:
        print(f"{numero1} e {numero2} e {numero3}")
    elif numero1 > numero2:
     print(f"{numero2} e {numero1} e {numero3}")
    else:
     print(f"{numero1} e {numero2} e {numero3}")
else:
    print(f"{numero1} e {numero2} e {numero3}")