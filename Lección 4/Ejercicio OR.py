lVacacion = bool(int(input("¿Hoy es día de vacaciones? (1 = SI, 0 = NO): ")))
lDescanso = bool(int(input("¿Hoy es día de descanso? (1 = SI, 0 = NO): ")))

if lVacacion or lDescanso:
    print("Hoy es día libre.")
else:
    print("Hoy es día de trabajo.")