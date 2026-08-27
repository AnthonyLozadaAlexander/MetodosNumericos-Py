import numpy as np
import matplotlib.pyplot as plt

k: int = 10  # constante escalar
ejeX: np.ndarray = np.array([1, 2, 3, 4])
ejeY: np.ndarray = ejeX * k

plt.plot(ejeX, ejeY, marker="o", color="blue")

plt.show()
