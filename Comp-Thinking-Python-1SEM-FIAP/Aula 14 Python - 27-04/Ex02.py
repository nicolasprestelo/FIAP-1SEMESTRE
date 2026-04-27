cont = 1
somatoria = 0

while cont < 1000:
    if cont % 3 == 0:
        somatoria += cont
    elif cont % 5 == 0:
        somatoria += cont
    cont += 1
print(somatoria)