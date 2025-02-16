# List Comprehension es un concepto con el cual, mediante el uso de expresiones generadoras, podemos crear una nueva lista
# basada en una lista existente. Además, la creación de esta nueva lista se lleva a cabo de una manera corta y eficaz

# Ejemplo (Creación de una Lista con Número Pares Exclusivamente):
listaNumeros = range(11)
listaNumerosPares = []

    # Manera Normal de Resolución:
for numero in listaNumeros:
    if numero % 2 == 0:
        listaNumerosPares.append(numero)
print(f'Lista de Números Pares Creada Normalmente: {listaNumerosPares}')

    # Resolución Mediante List Comprehension:
listNumerosPares = []
listNumerosPares = [value for value in listaNumeros if value % 2 == 0]
print(f'Lista de Números Pares Creada Usando List Comprehension: {listaNumerosPares}')
