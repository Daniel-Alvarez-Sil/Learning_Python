#Definición
diccionario = {
    "IDE":"Integrated Development Environment",
    "OOP":"Object Oriented Programming",
    "DBMS":"Database Management System"
}
print(f'Diccionario: {diccionario}')

#Longitud
print(f'Longitud: {len(diccionario)}')

#Acceder a un Elemento Mediante su LLAVE(KEY)
print(f'Elemento Individual: {diccionario["IDE"]}')
print(f'Elemento Individual: {diccionario.get("OOP")}')

#Modificar Elementos
diccionario["IDE"] = "Elemento Modificado"
print(f'Diccionario Modificado: {diccionario}')

#Consulta de ITEMS
print("Consulta de Llaves y Valores: ")
for c in diccionario.items():
    print("     ", c)

#Consulta de KEYS
print("Consulta de Llaves: ")
for c in diccionario.keys():
    print("       ", c)

#Consulta de VALUES
print("Consulta de Valores: ")
for c in diccionario.values():
    print("             ", c)

#Validación de Presencia del X Elemento
print(f'Existe el Elemento "IDE": {"IDE" in diccionario}')

#Agregar un Nuevo Elemento
diccionario["PK"] = "Primary Key"
print(f'Adición de Nuevo Elemento: {diccionario}')

#Remover Elementos por Llave
diccionario.pop("PK")
print(f'Elimación de Elemento: {diccionario}')

#Limpiar Diccionario
diccionario.clear()
print(f'Diccionario Limpio: {diccionario}')

#Eliminar Diccionario
del diccionario
print(diccionario)
