import numpy as np
import matplotlib.pyplot as plt

x: np.ndarray = np.linspace(-4, 4, 100)
y: np.ndarray = x**3 - 2 * x

y_derivada: np.ndarray = x - 2  # recta tangente de x^3 - 2x

plt.plot(x, y, label="f(x) = x^3 - 2x")  # funcion f(x) = x^3 - 2x
plt.plot(
    x, y_derivada, label="Derivada:  y = 3x^2 - 2"
)  # grafica la funcion de la derivada

plt.scatter(1, -1, color="blue", s=50, zorder=5, label="Punto (1, -1)")
# plt.scatter(1, 1, color="red", s=50, zorder=5, label="Punto (1, 1)")

plt.legend()
plt.grid(True)
plt.show()
