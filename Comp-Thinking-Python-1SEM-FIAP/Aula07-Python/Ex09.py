lado1 = float(input("Digite um número correspondente ao lado de um triângulo: "))
lado2 = float(input("Digite outro número correspondente ao outro lado de um triângulo: "))
lado3 = float(input("Digite outro número correspondente ao último lado de um triângulo: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero, ou seja, tem todos os lados iguais.")
elif lado1 == lado2 or lado3 == lado1 or lado3 == lado2:
    print("O triângulo é isósceles, ou seja, tem dois lados iguais.")
else:
    print("O triângulo é escaleno, não pussui lados iguais.")