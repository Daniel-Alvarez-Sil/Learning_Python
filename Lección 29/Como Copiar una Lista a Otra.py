# Módula para Leer y Asignar Información a una Dirección de Memoria
import ctypes

# Formas de Copiar un Lista (Crear una Lista en una Nueva Dirección de Memoria con la Información de otra Lista)
# NOTA: Todas estas formas de copiar crean una SHALLOW COPY 
# Una SHALLOW COPY se refiere a una copia en la cual el elemento copiado recibe referencias (direcciones en memoria)
# de los elementos del elemento original
lista1 = [1,2,3,4,5,6,7,8,9,10]

    # Método .copy() de la clase list
    # Este Método crea una SHALLOW COPY de una lista

lista2 = lista1.copy()

print(f'Dirección de Memoria de la Lista 1: {id(lista1)}\nDirección de Memoria de la Lista 2: {id(lista2)}')
for elemento1 in lista1:
    print(f'Dirección en Memoria del Elemento({elemento1}) de la Lista 1: {id(elemento1)}')
    print(f'Dirección en Memoria del Elemento({lista2[lista1.index(elemento1)]}) de la lista 2: {id(lista2[lista1.index(elemento1)])}')

    # Mediante el uso del constructor list
lista2 = list(lista1)
print(f'Dirección de Memoria de la Lista 1: {id(lista1)}\nDirección de Memoria de la Lista 2: {id(lista2)}')
for elemento1 in lista1:
    print(f'Dirección en Memoria del Elemento({elemento1}) de la Lista 1: {id(elemento1)}')
    print(f'Dirección en Memoria del Elemento({lista2[lista1.index(elemento1)]}) de la lista 2: {id(lista2[lista1.index(elemento1)])}')

    # Mediante el Uso de Slicing
    # SLICING es el método por el cual se iteran todos los elementos de una colección de datos
lista2 = lista1[:]
print(f'Dirección de Memoria de la Lista 1: {id(lista1)}\nDirección de Memoria de la Lista 2: {id(lista2)}')
for elemento1 in lista1:
    print(f'Dirección en Memoria del Elemento({elemento1}) de la Lista 1: {id(elemento1)}')
    print(f'Dirección en Memoria del Elemento({lista2[lista1.index(elemento1)]}) de la lista 2: {id(lista2[lista1.index(elemento1)])}')