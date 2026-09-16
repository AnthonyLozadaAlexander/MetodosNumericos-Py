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

mAnterior = (a + b) / 2
errorActual : float = 100.0

if(fx(a) * fx(mAnterior) < 0):
    b = mAnterior
else:
    a = mAnterior
    
while(errorActual > tolerancia):
    m = (a + b) / 2
    
    errorActual = error(m, mAnterior)
    
    mAnterior = m
    i += 1
    print("i: ", i)


xGen : np.ndarray = np.linspace(-1, 2, 100)
F : float = np.exp(2*xGen) - 6
plt.plot(xGen, F, label = "f(x) = e^(2x) - 6")
print("Resultado: ", m)
print("Error: ", errorActual)
plt.show()