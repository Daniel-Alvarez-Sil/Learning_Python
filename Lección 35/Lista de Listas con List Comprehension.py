# Rutina, con la cual desglosamos los elementos de las listas de una lista

listaDeListas = [[1,2,3], [4,5,6], [7,8,9,10]]
listaDesglosada = [valor for lista in listaDeListas for valor in lista]

print(f'Lista de Listas: {listaDeListas}')
print(f'Lista Desglosada: {listaDesglosada}')

# Creación de una Lista Desglosada de Números Pares
listaPares = [valor for lista in listaDeListas for valor in lista if valor % 2 == 0]
print(f'Lista Desglosada de Números Pares: {listaPares}')