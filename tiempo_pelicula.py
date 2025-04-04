duracion_pelicula = int(input("Ingrese la duración de la película (en minutos): "))
comerciales_previos = int(input("Ingrese la duración de los comerciales previos (en minutos): "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = int(input("Ingrese la duración de cada pausa comercial (en minutos): "))
total_comerciales_durante = cantidad_pausas * duracion_pausa
duracion_con_previos = duracion_pelicula + comerciales_previos
duracion_total = duracion_con_previos + total_comerciales_durante
print(f"\nDuración original de la película: {duracion_pelicula} minutos")
comerciales_totales = comerciales_previos + total_comerciales_durante
print(f"Duración total de los comerciales: {comerciales_totales} minutos")
print(f"Tiempo total de la proyección: {duracion_total} minutos")