import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x1: float = np.pi
x = sp.symbols("x")
f = x * (sp.cos(x))  # funcion
df = sp.diff(f, x)  # derivada
m = df.subs(x, x1)  # pendiente en el punto x1

m_num: float = float(m)  # type: ignore # convertir a float

fx = x1 * (np.cos(x1))
print("fx = ", fx)
print("m = ", m_num)

xGen: np.ndarray = np.linspace(-6, 10, 100)
y: np.ndarray = xGen * np.cos(xGen)  # funcion f(x) = sin(x)

y_derivada: np.ndarray = m_num * (xGen - x1) + fx  # recta tangente de sin(x)

plt.plot(xGen, y, label="f(x) = xcos(x)")
plt.plot(xGen, y_derivada, label="Derivada: y = cos(x) - xsin(x)")
plt.axhline(0, color="Black", linewidth=1)  # linea que cruza el eje x
plt.axvline(0, color="Black", linewidth=1)  # linea que cruza el eje y

plt.scatter(
    x1, fx, color="Brown", s=30, zorder=5, label=f"x1 = ({round(x1,2)}, {round(fx, 2)})"
)  # punto evaluado en la funcion de color cafe


plt.legend()
plt.grid(True)
plt.show()
