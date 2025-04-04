peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
altura_cuadrado = altura * altura
imc = peso / altura_cuadrado
imc = round(imc * 100) / 100
print(f"\nPeso ingresado: {peso} kg")
print(f"Altura ingresada: {altura} m")
print(f"IMC calculado: {imc}")
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 24.9:
    clasificacion = "Peso normal"
elif imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
print(f"Clasificación del IMC: {clasificacion}")