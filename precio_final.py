precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))
descuento = (precio_original * porcentaje_descuento) / 100
precio_con_descuento = precio_original - descuento
porcentaje_iva = float(input("Ingrese el porcentaje de IVA (%): "))
iva = (precio_con_descuento * porcentaje_iva) / 100
precio_final = precio_con_descuento + iva
print("\nResumen de la operación:")
print(f"Precio original: ${precio_original:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento}%): -${descuento:.2f}")
print(f"Precio con descuento: ${precio_con_descuento:.2f}")
print(f"IVA ({porcentaje_iva}%): +${iva:.2f}")
print(f"Precio final: ${precio_final:.2f}")
