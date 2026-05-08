"""
#---------------------------------------------------
# Alterar um item da lista
lista = [5, 2, 1, 7, 89, 4, 10, 10, 10, 10]
lista[4] = 10
print(lista[4])
lista[0] = 20
print(lista)

#---------------------------------------------------
# Inserir um item no final da lista
lista.append(100)
print(lista)
lista.append(50)
print(lista)

# Inserir item em um índice específico
lista.insert(0, 67)
print(lista)
lista.insert(3, 24)
print(lista)


#----------------------------------------------------
# Remover o último item da lista
lista.pop()
print(lista)

# Remover o item da lista pelo índice
lista.pop(2)
print(lista)
lista.pop(4)
print(lista)

# Remover a primeira ocorrencai de um valor na lista
lista.remove(10)
print(lista)

#Verificar se um item exise na lista
numero = int(input("Número: "))
if numero in lista:
      lista.remove(numero)
else:
      print(f"O valor {numero} não está na lista.")
print(lista)

# Remover todas as ocorrencas de um item da lista
while 10 in lista:
      lista.remove(10)
print(lista)


#-------------------------------------------------

# Excluir todos os itens da lista
lista.clear()
print(lista)

#-------------------------------------------------
#Preencher lista com input do usuário (tamanho pré-definido)
lista = []
for i in range(5):
      numero = int(input("Informe um número: "))
      lista.append(numero)
print(lista)

#Preencher lista com input do usuário (tamanho não definido)
lista = []
while True:
      numero = int(input("Informe um número (digite -1 para finalizar): "))
      if numero < 0:
            break
      lista.append(numero)
print(lista)
"""
#-------------------------------------------------
#Percorrer itens da lista
lista = [5, 7, 2, 3, 1, 67, 8, 33]
for item in lista:
      print(item)


# Contar quantos números pares existem na lista
cont = 0
for item in lista:
      if item % 2 == 0:
            cont += 1
print(f"Quantidade de números pares: {cont}")

#------------------------------------------------
# Percorrer os índices da lista
lista = [5, 7, 2, 3, 1, 67, 8, 33]
for indices in range(len(lista)):               # 0, 1, 2, 3, 4, 5, 6, 7
      print(lista[indices])


# alterar todos os números pares para zero
for i in range(len(lista)):
      if lista[i] % 2 == 0:
            lista[i] = 0
print(lista)
#------------------------------------------------