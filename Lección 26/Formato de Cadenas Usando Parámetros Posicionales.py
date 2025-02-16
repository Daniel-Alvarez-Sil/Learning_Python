sNombre = 'Daniel Alvarez'
iEdad = 18

mensajeConFormato = 'Hola, soy %s y tengo %i años'%(sNombre, iEdad)
print(f'Impresión de un mensaje con formato previamente asignado: ')
print(f'\t{mensajeConFormato}\n')

persona = ('Daniel', 'Alvarez', 'Sil')
mensajeConFormato = 'Hola, soy %s %s %s'%persona
print(f'Impresión de un mensaje con formato previamente asignado: ')
print(f'\t{mensajeConFormato}\n')

persona = ('Daniel', 'Mexicano', 9500.50)
print(f'Hola, mi nombre es %s y soy %s. Mi sueldo es %0.3f'%persona)