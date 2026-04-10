#Verificar se uma letra é vogal ou consoante

letra = input("Digite uma letra: ")

match letra.upper():
    case "A" | "E" | "I" | "U" | "O":
        print("Vogal")
    case _:
        print("Consoante")