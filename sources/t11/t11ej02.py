import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x ** 2)

# Definimos el dominio con la función np.linspace, que crea un vector de puntos equiespaciados:
x = np.linspace(-1, 3, 100)

# Y representamos la función
plt.plot(x, f(x), label="Función f(x)")
plt.xlabel("Eje $x$")
plt.ylabel("$f(x)$")
plt.legend()
plt.title("Función $f(x)$")
plt.show()