# Preparando o ambiente
import numpy as np
import matplotlib.pyplot as plt

# Definindo os valores de x:
x = np.linspace(-2, 4, 100)
print(x)

# Construção gráfica:
y = 2 ** x
plt.plot(x, y, label = "f(x) = 2^x", color = "red")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Exponenciais")
plt.xlabel("Domínio da Função: valores de x")
plt.ylabel("Imagem da Função: valores de y")
plt.gca().set_facecolor("lightgray")
plt.show()

y = 3 ** x + 2
plt.plot(x, y, label = "f(x) = 3^x + 2", color = "red")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Exponenciais")
plt.xlabel("Domínio da Função: valores de x")
plt.ylabel("Imagem da Função: valores de y")
plt.gca().set_facecolor("lightgray")
plt.show()

y = (1/2) ** x -1
plt.plot(x, y, label = "f(x) = (1/2)^x - 1", color = "red")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Exponenciais")
plt.xlabel("Domínio da Função: valores de x")
plt.ylabel("Imagem da Função: valores de y")
plt.gca().set_facecolor("lightgray")
plt.show()

y = 5 ** x + 3
plt.plot(x, y, label = "f(x) = 5^x + 3", color = "red")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Exponenciais")
plt.xlabel("Domínio da Função: valores de x")
plt.ylabel("Imagem da Função: valores de y")
plt.gca().set_facecolor("lightgray")
plt.show()

y = 2.718281 ** x - 2
plt.plot(x, y, label = "f(x) = e^x - 2", color = "red")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Exponenciais")
plt.xlabel("Domínio da Função: valores de x")
plt.ylabel("Imagem da Função: valores de y")
plt.gca().set_facecolor("lightgray")
plt.show()