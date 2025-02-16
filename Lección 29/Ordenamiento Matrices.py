matrix = [[1,2,3], [7,8,9,10], [4,5,6]]
print(f'Matriz Original: {matrix}')

# Ordenar por Largura de los Objetos
matrix.sort(key = len)
print(f'Matriz Ordenada por Largura de los Objetos: {matrix}')

# Ordenamiento de Matrices usando funciones integradas de Python (BUILT-IN)
nombres = ['Paulina', 'Martin', 'Alfonso', 'Alonso']

    # Ordenar alfabéticamente de manera ascendente
nombres = sorted(nombres)
print(f'Nombres Ordenados Alfabéticamente: {nombres}')

    # Ordenar alfabéticamente de manera descendente
nombres = sorted(nombres, reverse = True)
print(f'Nombres Ordenados Alfabéticamente Descendentemente: {nombres}')

    # Ordenar por la cantidad de caracteres
nombres = sorted(nombres, key = len)
print(f'Nombres Ordenados por la Cantidad de Caracteres: {nombres}')

    # Revertir el orden de una lista (Esta función regresa un objeto iterable, por lo que hay que convertirlo a algún tipo de colección de datos)
nombres = list(reversed(nombres))
print(f'Lista de Nombres con el Orden Revertido: {nombres}')