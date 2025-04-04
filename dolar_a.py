dolares = float(input("Ingrese la cantidad en dólares: "))
tasa_euro = 0.91     # 1 dólar = 0.91 euros
tasa_libra = 0.78    # 1 dólar = 0.78 libras
tasa_yen = 151.24    # 1 dólar = 151.24 yenes
euros = dolares * tasa_euro
libras = dolares * tasa_libra
yenes = dolares * tasa_yen
print("\nConversión de monedas:")
print(f"Dólares ingresados: ${dolares:.2f}")
print(f"En euros: €{euros:.2f}")
print(f"En libras: £{libras:.2f}")
print(f"En yenes: ¥{yenes:.2f}")
