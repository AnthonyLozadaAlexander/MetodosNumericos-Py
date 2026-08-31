import numpy as np
import matplotlib.pyplot as plt

a: np.ndarray = np.array([2, 1])
b: np.ndarray = np.array([1, 3])

c: np.ndarray = a + b

plt.quiver(
    0,
    0,
    a[0],
    a[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Cyan",
    label="a = [2, 1]",
)
plt.quiver(
    a[0],
    a[1],
    b[0],
    b[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Yellow",
    label="b = [1, 3]",
)
plt.quiver(
    0,
    0,
    c[0],
    c[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="Blue",
    label="c = [3, 4]",
)

plt.xlim(-1, 5)
plt.ylim(-1, 5)

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.legend()
plt.grid()
plt.show()
