#Definición
planetas = {"Marte", "Venus", "Júpiter"}
print(f'Set: {planetas}')

#Longitud
print(f'Longitud: {len(planetas)}')

#Validar la Presencia de un Elemento
print(f'"Venus" está dentro del SET: {"Venus" in planetas}')

#Agregar un Elemento
planetas.add("Tierra")
print(f'Adición de Planeta: {planetas}')

#Duplicidad
planetas.add(("Tierra"))
print(f'Adición Repetida de Mismo Planeta: {planetas}')

#Eliminación de Elementos
    #Envío de Error si Elemento no Existe
planetas.remove("Tierra")
print(f'Eliminación de Elemento: {planetas}')
    #No Hay Envío de Error si Elemento no Existe
planetas.discard("Tierra")
print(f'Eliminación de Elemento: {planetas}')

#Limpiar SET
planetas.clear()
print(f'Set Vacío: {planetas}')

#Eliminar Set por Completo
del planetas
print(planetas)