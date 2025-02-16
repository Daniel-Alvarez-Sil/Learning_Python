edad = int(input("Ingresa tu edad: "))

#Forma 1
print('Forma de ejecución 1. ')

if (edad >= 20 and edad < 30):
    print('Tu estás en tus 20\'s.')
else:
    if (edad >= 30 and edad < 40):
        print('Tú estás en tus 30\'s.')
    else:
        print ('Edad fuera de rango.')

#Forma 2
print('Forma de ejecución 2.')

if (edad >= 20 and edad < 30):
    print('Tu estás en tus 20\'s.')
elif (edad >= 30 and edad < 40):
        print('Tú estás en tus 30\'s.')
else:
    print ('Edad fuera de rango.')
