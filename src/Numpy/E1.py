import numpy as np
import matplotlib.pyplot as plt

a: np.ndarray = np.array([-1, 2])
b: np.ndarray = np.array([3, 1])
c: np.ndarray = np.array([-2, -3])

ab: np.ndarray = a + b

r: np.ndarray = a + b + c

# vector A
plt.quiver(
    0,
    0,
    a[0],
    a[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Cyan",
    label="a = [-1, 2]",
)

# vector B
plt.quiver(
    a[0],
    a[1],
    b[0],
    b[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Yellow",
    label="b = [3, 1]",
)

# vector C
plt.quiver(
    ab[0],
    ab[1],
    c[0],
    c[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Blue",
    label="c = [-2, -3]",
)

# vector resultante
plt.quiver(
    0,
    0,
    r[0],
    r[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Red",
    label="r = [0, 0]",
)

plt.title(" Vector Resultante: r = [a] + [b] + [c]")
plt.xlim(-4, 5)  # eje x
plt.ylim(-1, 5)  # eje y

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.legend()
plt.grid()
plt.show()
