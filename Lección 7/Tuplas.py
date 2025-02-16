#Definición
frutas = ("Naranja", "Plátano", "Guayaba")
print(f'Tupla: {frutas}')

#Longitud de la Tupla
print(f'Longitud: {len(frutas)}')

#Acceso a Elementos
print(f'Elemento Individual: {frutas[0]}')

#Navegación Inversa
print(f'Navegación Inversa: {frutas[-1]} {frutas[-2]} {frutas[-3]}')

#Acceso a Rangos
print(f'Consulta con Rangos: {frutas[:2]}')

#Recorrido de Tupla con FOR
print("Recorrido de Tupla: ", end = "")
for fruta in frutas:
    print(fruta, end = " ")

#Cambiar Valor de la Tupla
listaFrutas = list(frutas)
listaFrutas[0] = "Pera"
frutas = tuple(listaFrutas)
print (f'\nCambio de Valores: {frutas}')

#Eliminar Tupla
del frutas
print(frutas)