print("--- Menu Matemático ---")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
opcao = int(input("Digite a sua opção: "))
numero1 = int(input("Digite o primeiro número qual deseja fazer a operação: "))
numero2 = int(input("Digite o segundo número qual deseja fazer a operação: "))
if opcao == 1:
    soma = numero1 + numero2
    print(f"A soma dos valores é de {soma}")
elif opcao == 2:
    subtracao = numero1 - numero2
    print(f"A subtração dos valores é de {subtracao}")
elif opcao == 3:
    multiplicacao = numero1 * numero2
    print(f"A multiplicação dos valores é de {multiplicacao}")
elif opcao == 4:
    divisao = numero1 / numero2
    print(f"A divisão dos valores é de {divisao}")
else:
    print("Opção inválida.")

