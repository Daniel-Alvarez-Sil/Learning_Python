#Definir una lista
lista = ["Juan", "Daniel", "Pablo", "Andrea"]

#Imprimir Lista Completa
print(f'{lista} \n')

#Imprimir Lista Completa Individualmente
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print("\n")

#Imprimir Lista Completa Individualmente a la Inversa
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

#Imprimir Longitud de la Lista
print (f'\nLongitud: {len(lista)}')

#Agregar un Elemento
lista.append("Patricio")
print(f'\n{lista}')

#Insertar un Elemento un Índice Específico
lista.insert(0, "Unicio")
print(f'\n{lista}')

#Remover un Elemento por Nombre
lista.remove("Unicio")
print(f'\n{lista}')

#Remover el Último Elemento de la Lista
lista.pop()
print(f'\n{lista}')

#Eliminar Elemento por Índice
del lista[0]
print(f'\n{lista}')

#Imprimir la Lista por Rango (el Último Valor del Rango no se Incluye)
print(f'\n{lista[0:2]}')
print(f'\n{lista[ :2]}')
print(f'\n{lista[0: ]}')

#Asignar Nuevo Valor a un Elemento de una Lista
lista[0] = "Intercambicio"
print(f'\n{lista}\n')

#Iteración de la Lista
for c in lista:
    print(c)
else:
    print("No hay más valores en la lista")
#Limpiar la Lista
lista.clear()
print(f'\n{lista}')

#Eliminar por Completo Lista
del lista
print(f'\n{lista}')