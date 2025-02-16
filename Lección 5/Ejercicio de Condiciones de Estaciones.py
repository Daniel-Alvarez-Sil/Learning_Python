iMes = int(input ("Ingresa un mes (1-12): "))
cEstacion = None

if iMes == 12 or iMes == 1 or iMes == 2:
    cEstacion = "Invierno"
    if iMes == 1:
        print("1")
    elif iMes == 2:
        print("2")
    else:
        print ("12")
elif iMes >= 3 and iMes <= 5:
    cEstacion = "Primavera"
    if iMes == 3:
        print("3")
    elif iMes == 4:
        print("4")
    else:
        print("5")
elif iMes >= 6 and iMes <= 8:
    cEstacion = "Verano"
    if iMes == 6:
        print("6")
    elif iMes == 7:
        print("7")
    else:
        print ("8")
elif iMes >= 9 and iMes <= 11:
    cEstacion = "Otoño"
    if iMes == 9:
        print("9")
    elif iMes == 10:
        print("10")
    else:
        print("11")

print (f'''
^
|

Mes   Estacion: {cEstacion} ''')