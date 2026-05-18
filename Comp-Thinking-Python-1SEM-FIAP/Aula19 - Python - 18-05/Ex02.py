def numero_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False


    divisor = 3
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True

numero = int(input("Digite um número: "))
print(numero_primo(numero))