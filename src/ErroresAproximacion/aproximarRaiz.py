# Algoritmo para aproximar la raiz cuadrada de 4


def calcular_error_aprox(valorActual: float, valorAnterior: float) -> float:
    distancia = abs((valorActual - valorAnterior) / valorActual)
    return distancia * 100


numeroObjetivo: float = 4.0
tolerancia: float = 0.5  # el error debe ser menor a la tolerancia
valorAnterior: float = 1.0
errorActual: float = 100.0
intento: int = 1

print("-" * 30)
print(f"Aproximacion de la raiz cuadrada de {numeroObjetivo}")
print("-" * 30)

while errorActual > tolerancia:
    valorActual: float = (valorAnterior + (numeroObjetivo / valorAnterior)) / 2

    errorActual = calcular_error_aprox(valorActual, valorAnterior)

    print(
        f"Intento {intento} | Aproximacion: {valorActual:.5f} | Error:  {errorActual:.5f} %"
    )

    valorAnterior = valorActual
    intento = intento + 1


print("-" * 30)
print(f"La raiz aproximada es: {valorActual:.5f} con un error de {errorActual:.5f}%")
