import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def fun(x: float) -> float:
    result: float = x**2 * np.exp(x)
    return result


def F(x: np.ndarray) -> np.ndarray:
    result: np.ndarray = x**2 * np.exp(x)
    return result


x1: float = 2
x = sp.symbols("x")
f = x**2 * sp.exp(x)  # funcion
df = sp.diff(f, x)  # derivada
m = df.subs(x, x1)  # pendiente en el punto x1

m_num: float = float(m)  # type: ignore # convertir a float

fx: float = fun(x1)
print("fx = ", fx)
print("m = ", m_num)

xGen: np.ndarray = np.linspace(-3, 4, 100)
y: np.ndarray = F(xGen)  # funcion f(x) = x**2 * np.exp(x)

y_derivada: np.ndarray = m_num * (xGen - x1) + fx  # recta tangente de x**2 * np.exp(x)

plt.plot(xGen, y, label="Tiempo(x) = x^2e^x")
plt.plot(xGen, y_derivada, label="Derivada: y = e^x(x^2 + 2x)")
plt.axhline(0, color="Black", linewidth=1)  # linea que cruza el eje x
plt.axvline(0, color="Black", linewidth=1)  # linea que cruza el eje y

plt.scatter(
    x1, fx, color="Blue", s=30, zorder=5, label=f"x1 = ({round(x1,2)}, {round(fx, 2)})"
)  # punto de la funcion


plt.legend()
plt.grid(True)
plt.show()
