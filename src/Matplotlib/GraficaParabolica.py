# f(x) = x^2 - 7x + 12
import numpy as np
import matplotlib.pyplot as plt

a: int = 1
b: int = -7
c: int = 12

x: np.ndarray = np.linspace(0, 10, 50)
y: np.ndarray = (a * x**2) + (b * x) + (c)

plt.plot(x, y, marker="o", color="green")
plt.title(f"f(x) = {a}x^2 {b}x  + {c}")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.grid()
plt.show()
