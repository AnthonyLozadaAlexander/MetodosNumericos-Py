

def calcularErrorAproximado(valor_actual: float, valor_anterior: float) -> float:

    error = abs((valor_actual - valor_anterior) / valor_actual)

    error_porcentaje = error * 100

    return error_porcentaje


intento1: float = 1.50
intento2: float = 1.65

errorCalculado = calcularErrorAproximado(intento2, intento1)
print(f"El error de nuestra aproximacion actual es del {errorCalculado:.2f}%")
