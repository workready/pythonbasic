import numpy as np
import matplotlib.pyplot as plt

def frecuencias(f1, f2):
    max_time = 0.5
    times = np.linspace(0, max_time, 1000)
    signal = np.sin(2 * np.pi * f1 * times) + np.sin(2 * np.pi * f2 * times)
    with plt.style.context("ggplot"):
        plt.plot(signal, label="Señal")
        plt.xlabel("Tiempo ($t$)")
        plt.title("Dos frecuencias")
        plt.legend()
        plt.show()
        
frecuencias(10, 100)