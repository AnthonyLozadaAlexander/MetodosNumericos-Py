# serie: Es resultado de la suma de todos los  elementos  de la sucesion.
# 3n

from matplotlib import pyplot as plt
import numpy as np

sumatoria: int = 0
n: int = 0

for n in range(1, 5):
    sumatoria = sumatoria + 3 * n
    print(f"n{n}: 3*{n} = {3*n} | sumatoria = {sumatoria}")

print(f"Suma Total De La Serie 3n: {sumatoria}\n")

x: np.ndarray = np.linspace(1, 5, 100)

y: np.ndarray = 3 * x # funcion de la serie 3n

plt.plot(x, y, label="y = 3n", color="blue")
plt.xlim(-1, 11)
plt.ylim(-1, 31)
plt.xlabel("n")
plt.ylabel("3n")
plt.legend()
plt.title("Serie de 3n")
plt.show()
