import numpy as np
import matplotlib.pyplot as plt

#Exercicio 3
#Definir os valores de x:

x = np.linspace(-10, 10, 100)
print(x)

# a)
y = 3*x + 2
plt.plot(x,
        y,
        label="Gráfico da Função: f(x) = 3x + 2",
        color="blue")
plt.legend()
plt.grid()
plt.title("Gráficos de Funções Polinomiais")
plt.show()


# b)
y  = -2*x + 1
plt.plot(x,
        y,
        label="Gráfico da Função: f(x) = -2x + 1",
        color="blue")
plt.legend()
plt.grid()
plt.title("Gráficos de Funções Polinomiais")
plt.show()

# c)
y = x**2 - 4*x + 3
plt.plot(x,
        y,
        label="Gráfico da Função: y = x² -4x + 3",
        color="blue")
plt.legend()
plt.grid()
plt.title("Gráficos de Funções Polinomiais")
plt.show()

# d)
y =  -x**2 + 2 * x + 1
plt.plot(x,
        y,
        label="Gráfico da Função: y = -x² + 2x + 1",
        color="blue")
plt.legend()
plt.grid()
plt.title("Gráficos de Funções Polinomiais")
plt.show()

# e)
y = x ** 3 - x
plt.plot(x,
        y,
        label="Gráfico da Função: y = x³ - x",
        color="blue")
plt.legend()
plt.grid()
plt.title("Gráficos de Funções Polinomiais")
plt.show()


