lVacaciones = bool(int(input("¿Hoy es día de vacaciones? (1 = SI, 0 = NO): ")))
lDescanso = bool(int(input("¿Hoy es día de descanso? (1 = SI, 0 = NO): ")))

if not (lVacaciones or lDescanso):
    print(f'Hoy es día de trabajo.')
else:
    print(f'Hoy es día de descanso.')