# Creación de una Lista

lista1 = list(range(1,4))
lista2 = list(range(4,7))
lista3 = list(range(7,10))

listasUnidas = [*lista1, *lista2, *lista3]

print(f'Lista Creada a Base de una Suma de Listas Usando Unpacking: {listasUnidas}')

# Creación de un Diccionario

diccionario1 = {'A' : 1, 'B' : 2, 'C' : 3}
diccionario2 = {'D' : 4, 'E' : 5, 'F' : 6}
diccionario3 = {'G' : 7, 'H' : 8, 'I' : 9}

diccionariosUnidos = {**diccionario1, **diccionario2, **diccionario3}

print(f'Diccionario Creado a Base de una Suma de Diccionarios Usando Unpacking: {diccionariosUnidos}')
