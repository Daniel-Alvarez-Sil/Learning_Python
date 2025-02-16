llaves = [1,2,3,4,5,0]
valores = ['A', 'B', 'C', 'D', 'E', 'Z']
diccionario = dict(zip(llaves, valores))
print(f'Diccionario: {diccionario}')

# Recuperar un Valor Indicando una Llave
print(f'Valor 1: {diccionario[1]}') # <-- Con esta sintáxis, si no se encuentra la llave indicada, se levantará una excepción (error)

# Método Get
# Con este método, podemos indicar un mensaje de error para usar cuando la llave indicada no exista
print(f'Valor 6: {diccionario.get(6, "La llave indicada no existe dentro del diccionario. ")}')
print(f'Valor 7: {diccionario.get(7)}') # <-- Con esta sintáxis, no se levanta un error cuando la llave no existe

# Método SetDefault
# Con este método, si la llave indicada no se encuentra, la llave indicada es insertada junto con el parámetro de valor
# default al diccionario
print(f'Valor 2: {diccionario.setdefault(2)}')
print(f'Valor 8: {diccionario.setdefault(8, "Letra")}')
print(f'Diccionario con un Nuevo Elemento Añadido(8): {diccionario}')

# Método Pprint (Pretty Print)
# Este método imprime objetos de una manera más ordenada (prettier)
from pprint import pprint
print(f'Impresión de Diccionario en Orden Ascendente'.center(len('Impresión de Diccionario en Orden Ascendente') + 16, '+'))
pprint(diccionario)
print(f'Impresión de Diccionario sin Orden'. center(len('Impresión de Diccionario sin Orden') + 26, '-'))
pprint(diccionario, sort_dicts=False)