import numpy as np
import matplotlib.pyplot as plt

x: np.ndarray = np.linspace(-10, 10, 100)
y: np.ndarray = x**2

y_derivada: np.ndarray = -4 * x - 4  #  pendiente en el punto x = -2 y = 4

plt.plot(x, y, label="f(x) = x^2")
plt.plot(x, y_derivada, label="Derivada: y =  -4x - 4")
plt.scatter(
    -2, 4, color="red", s=100, zorder=5, label="Punto (-2, 4)"
)  # punto en la funcion

plt.legend()
plt.grid(True)
plt.show()
