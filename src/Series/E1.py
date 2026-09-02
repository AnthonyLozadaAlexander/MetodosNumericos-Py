#  Un algoritmo genera claves de seguridad sumando números impares secuenciales. La regla de cada iteración es $2n - 1$. Calcula a lápiz y papel el valor de la serie para las primeras 4 iteraciones: $\sum_{n=1}^{4} (2n - 1)$


sum: int = 0
n: int = 0

for n in range(1, 5):
    sum += 2 * n - 1
    print(f"n{n}: 2*{n} - 1 = {2 * n - 1}")
    print(f"sumatoria = {sum}")

print(f"\nSuma Total De La Serie 2n - 1: {sum}\n")
