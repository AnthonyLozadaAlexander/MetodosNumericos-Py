def calcular_tolerancia(n: int) -> float:
    tolerancia: float = 0.0
    if n <= 0:
        return 0.0
    else:
        tolerancia = 0.5 * (10 ** (2 - n))

    return tolerancia


# Estás midiendo un terreno y el margen de error es flexible. Necesitas garantizar solo 2 cifras significativas. ¿Cuál será tu porcentaje máximo de tolerancia ($\epsilon_s$)?

n: int
n = 2

tolerancia_permitida: float
tolerancia_permitida = calcular_tolerancia(n)

print(f"Para {n} cifras , la tolerancia maxima permitida es: {tolerancia_permitida} %")
