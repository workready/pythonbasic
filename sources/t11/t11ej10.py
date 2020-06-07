import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 7, 1000)

fig = plt.figure()

plt.subplot(211)
plt.plot(x, np.sin(x))
plt.grid(False)
plt.title("Función seno")

plt.subplot(212)
plt.plot(x, np.cos(x))
plt.grid(False)
plt.title("Función coseno")


# Esto es para que no se solapen las dos gráficas. Ver https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots-in-matplotlib/9827848#9827848
plt.subplots_adjust(hspace = 0.9)

plt.show()