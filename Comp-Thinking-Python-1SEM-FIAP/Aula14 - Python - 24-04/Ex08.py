numero = int(input("Número: "))
eh_primo = True

for i in range(2, numero):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo:
    print(f"O número é primo")
else:
    print("Não é primo")