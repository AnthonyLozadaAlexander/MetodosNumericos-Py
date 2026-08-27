numero_decimal = 0.123456789

numero_redondeado = round(numero_decimal, 4)
error_redondeo = abs(numero_decimal - numero_redondeado)

print(f"Error de redondeo: {error_redondeo}")
