help(str.format)

sNombre = 'Daniel'
iEdad = 18
fSueldo = 2500.49

mensajeConFormato = 'Hola, soy {} y tengo {} años. Mi sueldo es: ${:.3f}'.format(sNombre, iEdad, fSueldo)
print(f'Impresión de mensaje con formato asignado mediante el método FORMAT: ')
print(f'\t{mensajeConFormato}\n')

mensajeConFormato = 'Hola, soy {2} y tengo {0} años. Mi sueldo es: ${1:.2f}'.format(iEdad, fSueldo, sNombre)
print(f'Impresión de mensaje con formato asignado mediante el método FORMAT: ')
print(f'\t{mensajeConFormato}\n')

mensajeConFormato = 'Hola, soy {n} y tengo {e} años. Mi sueldo es: ${s:.3f}'.format(n = sNombre, e = iEdad, s = fSueldo)
print(f'Impresión de mensaje con formato asignado mediante el método FORMAT: ')
print(f'\t{mensajeConFormato}\n')

diccionario = {'nombre' : sNombre, 'edad' : iEdad, 'sueldo' : fSueldo}
mensajeConFormato = 'Hola, soy {diccionario[nombre]} y tengo {diccionario[edad]} años. Mi sueldo es: ${diccionario[sueldo]:.2f}'.format(diccionario = diccionario)
print(f'Impresión de mensaje con formato asignado mediante el método FORMAT: ')
print(f'\t{mensajeConFormato}\n')