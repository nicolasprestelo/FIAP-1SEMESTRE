vogais = "A", "E", "I","O","U"

letra = input("Digite uma letra: ")

if letra.upper() in vogais:
    print("A sua letra é uma vogal")
else:
    print("A sua letra é uma consoante")