import numpy as np
import matplotlib.pyplot as plt

v: np.ndarray = np.array([4, 3])

# np.linaalg.norm() sirve para calcular la magnitud de un vector
magnitud: float = np.linalg.norm(v)

print(f"Magnitud: {magnitud}")

plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="green")
