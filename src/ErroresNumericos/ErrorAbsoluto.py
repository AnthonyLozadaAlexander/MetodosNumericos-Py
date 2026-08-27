# Error en valor exactos
valor_exacto: float
valor_aprox: float
error_absoluto: float

valor_exacto = 1 / 3
valor_aprox = 0.3333333
error_absoluto = abs(valor_exacto - valor_aprox)

print(f"Error Absoluto: {error_absoluto}")  # 3.333333331578814x10^-08
