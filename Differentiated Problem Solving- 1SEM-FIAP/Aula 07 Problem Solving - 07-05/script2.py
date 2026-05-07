import numpy as np
import matplotlib.pyplot as plt

# a)
def V(t):
    return 5 * (2**t)

t = np.arange(0, 11, 1)
volume = V(t)

# b)
print("t | V(t)")
for i in range(len(t)):
    print( t[i], "|", volume[i])

# c)
plt.plot(t, volume, label = "V(t) = 5.2^t", marker = "o", color = "yellow")
plt.legend()
plt.grid()
plt.title("Gráfico de Funções Exponenciais")
plt.xlabel("Domínio da Função: valores de t")
plt.ylabel("Imagem da Função: valores de V")
plt.gca().set_facecolor("lightgray")
plt.show()

