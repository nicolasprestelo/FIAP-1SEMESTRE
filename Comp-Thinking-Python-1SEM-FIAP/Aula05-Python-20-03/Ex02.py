caixa = 24
produtos = 1250

totalDeCaixas = produtos // caixa
produtosSobrando = produtos % caixa

print(f"Serão necessárias {totalDeCaixas} caixas e ficarão de fora {produtosSobrando} produtos. ")