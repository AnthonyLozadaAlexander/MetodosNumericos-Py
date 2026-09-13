import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

a: int = 1
b: int = 5

GenX: np.ndarray = np.linspace(-1, 11, 100)
y: np.ndarray = 3 * GenX

GenXI: np.ndarray = np.linspace(a, b, 100)
yI: np.ndarray = 3 * GenXI

x: float = sp.symbols("x")
f: float = 3 * x
I = sp.integrate(f, (x, a, b))
print("Area: ", I)

plt.plot(GenX, y, label="f(x) = 3x", color="red")

plt.fill_between(GenXI, yI, color="blue", alpha=0.5, label=f"Area: {I}")

plt.axhline(0, color="Black", linewidth=1)  # linea que cruza el eje x
plt.axvline(0, color="Black", linewidth=1)  # linea que cruza el eje y

plt.axvline(b, color="Orange", linewidth=1)  # linea que cruza el eje x
plt.axvline(a, color="Orange", linewidth=1)  # linea que cruza el eje y

plt.legend()
plt.show()
