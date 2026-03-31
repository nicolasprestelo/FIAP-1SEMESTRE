altura = float(input("Digite a altura do cômodo: "))
largura = float(input("Digite a largura do cômodo: "))
comprimento = float(input("Digite o comprimento do cômodo: "))

area_paredes = (comprimento * altura * 2) + (altura * largura * 2)
area_teto = largura * comprimento
area_total = area_paredes + area_teto
quantidade_tinta = area_total / 3

print(f"Será necessário {quantidade_tinta} litros de tinta para pintar as 4 paredes e o teto do cômodo.")