salario = float(input("Digite o valor do seu salário: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

if prestacao >= (salario * 0.2):
    print("Empréstimo não concedido.")

else:
    print("Empréstimo concedido.")