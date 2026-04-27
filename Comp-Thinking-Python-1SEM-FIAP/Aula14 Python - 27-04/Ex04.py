cont = 1000000

for numero in range(2, cont):
    verificar_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            verificar_primo = False
            break

        if verificar_primo:
            print(numero)

