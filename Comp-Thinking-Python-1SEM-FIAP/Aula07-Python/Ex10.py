salario_fixo = float(input("Digite o valor do seu salário fixo: "))
valor_vendas = float(input("Digite o valor das vendas efetuadas: "))


if valor_vendas <= 1500:
    salario_comissao = valor_vendas * 0.03
elif valor_vendas > 1500.00:
    valor_comissao5 = valor_vendas - 1500
    salario_comissao = (1500 * 0.03) + valor_comissao5 * 0.05

salario_total = salario_fixo + salario_comissao
print(f"O salário do funcionário é de: R${salario_total}")
