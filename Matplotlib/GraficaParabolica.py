# f(x) = x^2 - 7x + 12
import numpy as np
import matplotlib.pyplot as plt

x: np.ndarray = np.linspace(0, 10, 50)
y: np.ndarray = x**2 - 7 * x + 12

plt.plot(x, y, marker="o", color="green")
plt.title("f(x) = x^2 - 7x  + 12")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.grid()
plt.show()
