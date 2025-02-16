sNombre = 'Daniel'
iEdad = 18
fSueldo = 3500.75

mensajeConFormato = f'Hola, soy {sNombre} y tengo {iEdad} años. Mi sueldo es: {fSueldo:.04f}'
print(f'Impresión de mensaje con formato previamente asignado: ')
print(f'\t{mensajeConFormato}\n')

print(f'Impresión de mensaje con separación de comas: ')
print('\t')
print(sNombre, iEdad, fSueldo, sep = ', ')