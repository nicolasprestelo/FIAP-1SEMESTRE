def verificar_senha(senha):
    if len(senha) >= 8 and any(caractere.isdigit() for caractere in senha):
        return True
    else:
        return False

senha = input("Digite a sua senha: ")

print(verificar_senha(senha))