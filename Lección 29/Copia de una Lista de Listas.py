# Cuando una Lista de Listas es Copiada, es importante recordar que, al modificar una de las 2 listas (copia u original),
# ambas listas serán modificadas debido a que comparten una sola dirección de memoria

# Ejemplo de lo establecido anteriormente:
listaOriginal = [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
iIndex = 0
listaCopia = listaOriginal.copy()

print(f'Impresión de Información Antes de Modificar 1 de las 2 Listas'.center(50, '-'))
print(f'Dirección en Memoria de la Lista Original: {id(listaOriginal)}\nDirección en Memoria de la Lista Copia: {id(listaCopia)}')
for elemento in listaOriginal:
    print(f'Dirección en Memoria del Elemento({elemento}) de la Lista Original: {id(elemento)}')
    print(f'Dirección en Memoria del Elemento({listaCopia[iIndex]}) de la Lista Copia: {id(listaCopia[iIndex])}')
    iIndex = iIndex + 1

iIndex = 0
(listaOriginal[2])[1] = 5

print(f'Impresión de Información Después de Modificar 1 de las 2 Listas'.center(50, '-'))
print(f'Dirección en Memoria de la Lista Original: {id(listaOriginal)}\nDirección en Memoria de la Lista Copia: {id(listaCopia)}')
for elemento in listaOriginal:
    print(f'Dirección en Memoria del Elemento({elemento}) de la Lista Original: {id(elemento)}')
    print(f'Dirección en Memoria del Elemento({listaCopia[iIndex]}) de la Lista Copia: {id(listaCopia[iIndex])}')
    iIndex = iIndex + 1
