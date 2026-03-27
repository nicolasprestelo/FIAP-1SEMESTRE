horas = int(input("Digite um número inteiro para horas: "))
minutos = int(input("Digite outro número inteiro para minutos: "))

if horas > 23 or horas < 0:
    print("Horas inválidas. São válidas as horas entre 00:00 e 23:59")

elif minutos > 59 or minutos < 0:
        print("Horas inválidas. São válidas as horas entre 00:00 e 23:59")
else:
    print(f"Sua hora é válida: {horas}:{minutos}")