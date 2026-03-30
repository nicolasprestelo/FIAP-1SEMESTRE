lado_a = float(input("Digite o lado A do triângulo: "))
lado_b = float(input("Digite o lado B do triângulo: "))
lado_c = float(input("Digite o lado C do triângulo: "))

if lado_a <= lado_b + lado_c and lado_b <= lado_c + lado_a and lado_c <= lado_a + lado_b :
    print("Esses valores podem ser lados de um triângulo.")
else:
    print("Esses valores NÃO podem ser lados de um triângulo.")