llaves = ['Nombre', 'Apellido', 'Edad', 'Correo']
valores = ['Daniel', 'Alvarez', 18, 'mision.d.a.s.04@gmail.com']

diccionario = dict(zip(llaves, valores))

print(f'Diccionario: {diccionario}')

# Actualización de los valores del diccionario
llave = ['Edad']
valor = [19]
diccionario.update(zip(llave, valor)) # =  d.update(Edad = 19)
print(f'Diccionario: {diccionario}')