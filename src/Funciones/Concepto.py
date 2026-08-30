import numpy as np
import matplotlib.pyplot as plt


def f(x: float) -> float:
    result: float = 3 * x - 5
    return result


def F(x: np.ndarray) -> np.ndarray:
    result: np.ndarray = 3 * x - 5
    return result


x: float = 2.0  # Punto A Evaluar En La Funcion
print(f"f({x}) = {f(x)}")  # funcion que devuelve el valor de la funcion el punto x

xGen: np.ndarray = np.linspace(-5, 5, 100)
y: np.ndarray = F(xGen)
plt.plot(xGen, y, label="f(x) = 3x - 5")

plt.axhline(0, color="Black", linewidth=1)
plt.axvline(0, color="Black", linewidth=1)
plt.scatter(x, f(x), color="Red", s=30, zorder=5, label=f"x  = ({x}, {round(f(x), 2)})")


plt.grid(True)
plt.legend()
plt.show()
