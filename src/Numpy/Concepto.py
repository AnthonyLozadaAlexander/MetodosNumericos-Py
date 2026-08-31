import numpy as np
import matplotlib.pyplot as plt

v: np.ndarray = np.array([4, 3])

# np.linaalg.norm() sirve para calcular la magnitud de un vector
magnitud: float = np.linalg.norm(v)

print(f"Magnitud: {magnitud}")

plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="Blue")


plt.xlim(-1, 5)
plt.ylim(-1, 5)

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.scatter(v[0], v[1], color="Red", label=f"x = {v[0]}, y = {v[1]}")
plt.legend()
plt.grid()

plt.title("Vector V = [4, 3]")
plt.show()
