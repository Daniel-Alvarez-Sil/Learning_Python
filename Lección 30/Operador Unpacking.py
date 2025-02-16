# El operador unpacking es '*' y sirve para separar los elementos de una colección de datos
# Si la coleccion de datos es de tipo diccionario, el operador unpacking correspondiente es '**'

lista = [1,2,3,4]
print(f'Impresión de Lista Normal: {lista}')

print(f'Unpacking de Lista Previa: ')
print(*lista)

diccionario = {'uno' : 1, 'dos' : 2, 'tres' : 3}
print(f'Impresión de Diccionario Normal: {diccionario}')

print(f'Unpacking de Diccionario Previo: ')
print(*diccionario)

