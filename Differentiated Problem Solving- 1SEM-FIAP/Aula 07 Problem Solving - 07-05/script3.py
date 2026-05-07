import numpy as np
import matplotlib.pyplot as plt

# Definir valores de x:
x = np.linspace(0.1, 5, 100)

# Construção Gráfica
y = np.log2(x)

plt.plot(x, y, label = "f(x) = log2 (x)",marker ="x", color = "lightblue")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Logarítmicas")
plt.xlabel("Domínio da Função: valores de x")
plt.ylabel("Imagem da Função: valores de Y")
plt.gca().set_facecolor("lightyellow")
plt.show()
