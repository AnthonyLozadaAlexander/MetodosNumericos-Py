import numpy as np
import matplotlib.pyplot as plt

x: np.ndarray = np.linspace(0, 6, 100)

y: np.ndarray = x**2  # funcion f(x) = x^2
y_derivada: np.ndarray = 6 * x - 9  # tangente: y = 6x - 9

plt.plot(x, y, label="f(x) = x^2")
plt.plot(x, y_derivada, label="Derivada: y = 6x - 9")

plt.legend()

plt.show()
