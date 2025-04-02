"""
calcule l nota de un estudiante, que 
tiene 2 sistemas de 30 
y uno de 40
"""
sistematico1 = int(input("ingrese el primer sistematico(maximo 30): "))
sistematico2 = int(input("ingrese el segundo sistematico(maximo 30): "))
sistematico3 = int(input("ingrese el tercer sistematico(maximo 40): "))
nota = (sistematico1 + sistematico2 + sistematico3)
print("la nota del estudiante es: ", nota)