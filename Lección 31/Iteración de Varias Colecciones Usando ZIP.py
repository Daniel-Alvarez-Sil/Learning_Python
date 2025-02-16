lista = [1,2,3,4,5]
tupla = ('A', 'B', 'C', 'D')
conjunto = {'Daniel', 'Armando', 'Juan', 'Luis', 'Andrea', 'Blanca', 'Emiliano'}
nuevaLista = []

for numero, letra, nombre in zip(lista, tupla, conjunto):
    print(f'Elementos de las Colecciones: {numero}, {letra}, {nombre}')
    nuevaLista.append(f'{numero}.- {letra}: {nombre}')

print(f'\nImpresión de Nueva Lista: \n')
for elemento in nuevaLista:
    print(f'Elemento: {elemento}')