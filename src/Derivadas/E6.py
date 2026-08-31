import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def fun(x: float) -> float:
    result: float = 2 * (x**3) - 4 * (x**2) + 5 * x + 12
    return result


def F(x: np.ndarray) -> np.ndarray:
    result: np.ndarray = 2 * (x**3) - 4 * (x**2) + 5 * x + 12
    return result


x1: float = 3
x = sp.symbols("x")
f = 2 * (x**3) - 4 * (x**2) + 5 * x + 12  # funcion
df = sp.diff(f, x)  # derivada
m = df.subs(x, x1)  # pendiente en el punto x1

m_num: float = float(m)  # type: ignore # convertir a float

fx: float = fun(x1)
print("fx = ", fx)
print("m = ", m_num)

xGen: np.ndarray = np.linspace(-6, 10, 100)
y: np.ndarray = F(xGen)  # funcion f(x) = 2 * (x**3) - 4 * (x**2) + 5 * x + 12

y_derivada: np.ndarray = (
    m_num * (xGen - x1) + fx
)  # recta tangente de 2 * (x**3) - 4 * (x**2) + 5 * x + 12

plt.plot(xGen, y, label="Tiempo(x) = 2x^3 - 4x^2 + 5x + 12")
plt.plot(xGen, y_derivada, label="Derivada: y = 6x^2 - 8x + 5")
plt.axhline(0, color="Black", linewidth=1)  # linea que cruza el eje x
plt.axvline(0, color="Black", linewidth=1)  # linea que cruza el eje y

plt.scatter(
    x1, fx, color="Blue", s=30, zorder=5, label=f"x1 = ({round(x1,2)}, {round(fx, 2)})"
)  # punto de la funcion


plt.legend()
plt.grid(True)
plt.show()
