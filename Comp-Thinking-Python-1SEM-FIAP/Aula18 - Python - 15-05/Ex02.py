
def lados_poligono(numero_lados):
    if numero_lados == 3:
        print("TRIÂNGULO")
    elif numero_lados == 4:
        print("QUADRILÁTERO")
    elif numero_lados == 5:
        print("PENTÁGONO")
    else:
        print("VALOR INVÁLIDO")

lados_poligono(5)