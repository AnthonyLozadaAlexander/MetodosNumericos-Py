import numpy as np

result: np.ndarray
arreglo1: np.ndarray = np.array([1, 2, 3, 4])
k: int = 10

result = arreglo1 + k
print("Arreglo 1: ", arreglo1)
print(f"Escalar K: {k}")

print(f"Arreglo + k = {result}")


arreglo2: np.ndarray = np.array([2, 2, 2, 2])
producto: np.ndarray = arreglo1 * arreglo2

print(f"\nA = ", arreglo1)
print(f"B = ", arreglo2)
print(f"Producto de [A] * [B] = {producto}")
