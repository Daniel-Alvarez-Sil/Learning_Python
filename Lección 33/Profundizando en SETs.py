# SETs
# Los elementos de un SET son únicos y todos los SETs son mutables
# Los elementos de un SET deben ser hashables

# Set Vacío:
setVacio = set()
print(f'Set vacío: {setVacio}')

# Mutabilidad:
setVacio.add('Nuevo Miembro')
print(f'Set con un Elemento Añadido: {setVacio}')

# Unicidad de los Elementos:
setVacio.add('Nuevo Miembro')
print(f'Set con un Miembro Agregado: {setVacio}')

# Creación de un SET a Partir de una Iterable
conjunto = set([1,2,3,4,5,1,2,3,4])
print(f'Impresión de Set Creado a Partir de una Iterable: {conjunto}')

# Añadir a un SET una colección
conjunto.update({6,7,8,9,10})
print(f'Impresión del Set al que Se le Ha Añadido otro Set: {conjunto}')

conjunto.update([11,12,13,14,15])
print(f'Impresión del Set al que Se le Ha Añadido la Información de una Lista: {conjunto}')

# Realizar una Shallow Copy de un SET
conjuntoCopia = conjunto.copy()
print(f'Impresión de la Copia del Set: {conjuntoCopia}')