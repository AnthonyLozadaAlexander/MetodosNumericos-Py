import numpy as np
import matplotlib.pyplot as plt

def error(a : float, b : float) -> float:
    return (abs(a - b) / a) * 100

def fx(x : float) -> float:
    return np.exp(2*x) - 6

def calcular_tolerancia(n: int) -> float:
    tolerancia: float = 0.0
    if n <= 0:
        return 0.0
    else:
        tolerancia = 0.5 * (10 ** (2 - n))

    return tolerancia

tolerancia : float = calcular_tolerancia(5)
a : float = 0.8
b : float = 0.9
i : int = 0

errorActual : float = 100.0
while(errorActual > tolerancia):
    m_Anterior = (a + b) / 2

    if(fx(a) * fx(m_Anterior) < 0):
        b = m_Anterior
    else:
        a = m_Anterior

    m = (a + b) / 2
    
    errorActual = error(m, m_Anterior)
    
    i += 1
    print(f"i: {i}")


xGen : np.ndarray = np.linspace(-1, 2, 100)
F : float = np.exp(2*xGen) - 6
plt.plot(xGen, F, label = "f(x) = e^(2x) - 6")
plt.scatter(m, fx(m), color = "red", label = f"Raiz Aproximada: {m:.5f}")

print(f"Resultado: {m:.5f}")
print(f"Error:  {errorActual:.5f}")

plt.legend()
plt.show()
