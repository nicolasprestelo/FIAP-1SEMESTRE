while True:
    X = int(input("Informe o primeiro número: "))
    Y = int(input("Informe o segundo número: "))
    if Y < X:
        print("O segundo número não pode ser menor que o primeiro.")
    else:
        break
while X < Y:
    if X % 2 == 0:
        X += 1
    else:
        print(f"Número ímpar no intervalo de X e Y: {X}")
        X += 1