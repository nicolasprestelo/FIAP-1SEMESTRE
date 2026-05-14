# Preparando o ambiente:
import numpy as np
import matplotlib.pyplot as plt

# Calculand sen(90°):
# Calculo em  Graus:
print(np.sin(np.radians(90)))

# Calculo em pi radianos:
print(np.sin(np.pi/2))

# Exercicio 1:
# a) y = sen(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

y = np.sin(x)

plt.plot(x, y, marker = '.',  label = "f(x) = sen(x)", color = "white")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Trigonométrica")
plt.xlabel("Domínio da Função: Valores de x")
plt.ylabel("Imagem da Função: Valores de y")
plt.gca().set_facecolor("black")
plt.show()


# Exercicio 2:
# b) f(x) = cos(x)

y = np.cos(x)

plt.plot(x, y, marker = '.',  label = "f(x) = cos(x)", color = "white")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Trigonométrica")
plt.xlabel("Domínio da Função: Valores de x")
plt.ylabel("Imagem da Função: Valores de y")
plt.gca().set_facecolor("black")
plt.show()


# Exercicio 3:
# C) y = 2 * sen(3x)

y = 2 * np.sin(3 * x)
plt.plot(x, y, marker = '.',  label = "y = 2 * sen(3x)", color = "white")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Trigonométrica")
plt.xlabel("Domínio da Função: Valores de x")
plt.ylabel("Imagem da Função: Valores de y")
plt.gca().set_facecolor("black")
plt.show()


#Exercicio 4:
# D) f(x) = -4cos(5x) + 2

y = -4 * np.cos(5 * x) + 2
plt.plot(x, y, marker = '.',  label = "f(x) = -4cos(5x) + 2", color = "white")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Trigonométrica")
plt.xlabel("Domínio da Função: Valores de x")
plt.ylabel("Imagem da Função: Valores de y")
plt.gca().set_facecolor("black")
plt.show()


#Exercicio 5:
#E) y = 3sen(2x - pi) -5

y = 3 * np.sin(2*x - np.pi) - 5
plt.plot(x, y, marker = '.',  label = "y = 3sen(2x - pi) -5", color = "white")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Trigonométrica")
plt.xlabel("Domínio da Função: Valores de x")
plt.ylabel("Imagem da Função: Valores de y")
plt.gca().set_facecolor("black")
plt.show()



