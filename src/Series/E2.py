# Reto 4 (Paginación de Memoria): Un sistema operativo asigna bloques de RAM con saltos fijos. Las direcciones de inicio de los primeros 5 bloques son: 0, 4, 8, 12, 16. Encuentra la regla para el término $n$ y calcula la serie de estas 5 iteraciones. (Pista: fíjate qué pasa si a la regla $4n$ le restas 4).

result = [(4 * n - 4) for n in range(1, 6)]

print(result)
