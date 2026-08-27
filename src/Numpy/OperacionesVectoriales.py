import numpy as np

result: np.ndarray
arreglo1: np.ndarray = np.array([1, 2, 3, 4])
k: int = 10

result = arreglo1 + k
print("Arreglo 1: ", arreglo1)
print(f"Escalar K: {k}")

print(f"Arreglo + k = {result}")
