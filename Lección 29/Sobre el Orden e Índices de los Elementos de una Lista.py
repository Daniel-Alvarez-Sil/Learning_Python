lista = [1,2,4,3,6,5,8,7,9,10]
print(f'Lista original: {lista}')

# Cómo encontrar el índice de la primera aparición de un elemento en una lista
print(f'El elemento \'10\' ocupa el índice {lista.index(10)}')

# Invertir el orden de los elementos de una lista
listaRevertida = lista
listaRevertida.reverse()
print(f'Lista revertida: {listaRevertida}')

# Ordenar los elementos de una lista de manera ascendente
listaAscend = lista
listaAscend.sort()
print(f'Lista ordenada, de manera ascendente: {listaAscend}')

# Ordenar los elementos de una lista de manera descendente
listaDescend = lista
listaDescend.sort(reverse = True)
print(f'Lista ordenada, de manera descendente: {listaDescend}')
