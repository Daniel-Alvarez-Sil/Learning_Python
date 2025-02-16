help(str.join)

# Ejemplo con Tuplas:
tuplaPalabras = ('Hola', 'Mundo', 'de', 'Python')
mensaje = ' '.join(tuplaPalabras) # <-- Sintáxis: <cadena a ingresar entre cada elemento de la iterable>.join(<iterable>)
                                  # <-- NOTA:     Todos elementos de la iterable deben ser de tipo caracter
print(f'Unión de los elementos de una tupla: {mensaje}')

# Ejemplo con Listas:
listaPalabras = ['Daniel', 'Danna', 'Mariana', 'Alex', 'Jose']
mensaje = ', '.join(listaPalabras)
print(f'Unión de los elementos de una lista: {mensaje}')

# Ejemplo con Strings:
stringPalabra = 'HOLAATODOS'
mensaje = ' '.join(stringPalabra)
print(f'Unión de los caracteres de un string: {mensaje}')

# Ejemplo con Diccionarios:
diccionario = {'Nombre':'Daniel', 'Apellido':'Alvarez', 'Edad':'18'}
mensaje = ' - '.join(diccionario.keys())
print(f'Unión de las llaves de un diccionario: {mensaje}')
mensaje = ' - '.join(diccionario.values())
print(f'Unión de los valores de un diccionario: {mensaje}')
