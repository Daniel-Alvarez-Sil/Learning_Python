# Diccionarios

# Orden
# A partir de la versión 3.7 de Python, los diccionarios son objetos con orden
llaves = ['Nombre', 'Apellido', 'Edad', 'Correo']
valores = ['Daniel', 'Alvarez', 19, 'mision.d.a.s.04@gmail.com']
diccionario = dict(zip(llaves, valores))
print(f'Diccionario con Orden: {diccionario}')

# Mutabilidad
# Los diccionarios son mutables, pero sus llaves deben estar constituidas por objetos hashables
# diccionario.update({[1,2] : 'Prueba'}) # <-- Esta sintáxis es incorrecta porque no puede haber una llave no hashable
diccionario.update({(1,2) : 'Prueba'})
print(f'Diccionario con una Lista como una Llave: {diccionario}')

# Adición
# Se puede añadir otro elemento al diccionario de la siguiente manera:
# NOTA: Si la llave ya existe, simplemente se actualizará su información, ya que no puede haber duplicidad de llaves
diccionario['Departamento'] = 'Sistemas'
print(f'Diccionario con un Nuevo Elemento Añadido: {diccionario}')

diccionario['Nombre'] = 'Danielle'
print(f'Diccionario con un Elemento Actualizado: {diccionario}')