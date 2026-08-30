import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x1: float = 0
x = sp.symbols("x")
f = sp.sin(x)  # funcion
df = sp.diff(f, x)  # derivada
m = df.subs(x, x1)  # pendiente en el punto x1

m_num: float = float(m)  # convertir a float

fx = np.sin(x1)
print("fx = ", fx)
print("m = ", m_num)

xGen: np.ndarray = np.linspace(-3, 3, 100)
y: np.ndarray = np.sin(xGen)  # funcion f(x) = sin(x)

y_derivada: np.ndarray = m_num * (xGen - x1) + fx  # recta tangente de sin(x)

plt.plot(xGen, y, label="f(x) = sin(x)")
plt.plot(xGen, y_derivada, label="Derivada: y = cos(x)")
plt.axhline(0, color="Black", linewidth=1)  # linea que cruza el eje  x

plt.scatter(
    x1, fx, color="Blue", s=30, zorder=5, label=f"x1 = ({x1}, {round(fx)})"
)  # punto de la uncion
plt.scatter(
    x1 + m_num,
    fx + m_num,
    color="Red",
    s=30,
    zorder=5,
    label=f"m = ({round(x1+m_num, 2)},{round(fx+ m_num, 2)})",
)

plt.legend()
plt.grid(True)
plt.show()
