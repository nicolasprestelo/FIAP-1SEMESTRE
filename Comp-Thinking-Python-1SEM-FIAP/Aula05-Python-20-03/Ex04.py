tempoSegundos = int(input("Digite um valor de tempo em segundos: "))
conversaoHoras = tempoSegundos // 3600
conversaoMinutos = (tempoSegundos % 3600) / 60
print(f"O seu tempo de {tempoSegundos}s equivale a {conversaoHoras} horas e {conversaoMinutos} minutos.")