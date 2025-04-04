tramo1 = float(input("Duración del primer tramo del vuelo (en horas): "))
escala1 = float(input("Duración de la primera escala (en horas): "))
tramo2 = float(input("Duración del segundo tramo del vuelo (en horas): "))
escala2 = float(input("Duración de la segunda escala (en horas): "))
tramo3 = float(input("Duración del tercer tramo del vuelo (en horas): "))
total = tramo1 + escala1
total += tramo2
total += escala2
total += tramo3
print(f"\nEl tiempo total del viaje es de {total:.2f} horas.")