import numpy as np
import matplotlib.pyplot as plt

k: int = 10  # constante escalar
ejeX: np.ndarray = np.array([1, 2, 3, 4])
ejeY: np.ndarray = ejeX * k

plt.plot(
    ejeX, ejeY, marker="o", color="blue"
)  # Le pasamos el eje x y eje y, y marcamos en cada punto con un circulo y de color azul a la linea

# Asignamos titulo y texto a las etiquetas de los ejes.
plt.title(f"f(x) = {k} * x")
plt.xlabel(" Eje X (Valores Entrada)")
plt.ylabel(" Eje Y (Valores Salida)")

# agregamos la cuadricula
plt.grid()

plt.show()  # mostrar la grafica
