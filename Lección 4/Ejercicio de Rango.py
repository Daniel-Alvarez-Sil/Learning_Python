iMin = 0
iMax = 5

iValor = int(input("Ingresa un valor: "))

rango = (iMin <= iValor) and (iMax >= iValor)

if rango:
    print(f'El valor {iValor} esta dentro de rango.')
else:
    print(f'El valor {iValor} esta fuera de rango.')