# Creación de 2 Listas, Una con Números Pares y la Otra con Números Impares

listaNumPares = []
listaNumImpares = []

    # Resolución Normal
for numero in range(21):
    if numero % 2 == 0:
        listaNumPares.append(numero)
    else:
        listaNumImpares.append(numero)

print(f'Creación de las Listas de Manera Normal'.center(56, '-'))
print(f'Números Pares: {listaNumPares}')
print(f'Numeros Impares: {listaNumImpares}')

print()

    # Resolución Usando List Comprehension
listaNumPares = []
listaNumImpares = []
[listaNumPares.append(numero) if numero % 2 == 0 else listaNumImpares.append(numero) for numero in range(21)] # <-- La expresión generadora se encierra con paréntesis para que dicha función sea consumada
print(f'Creación de las Listas Usando List Comprehension'.center(56, '+'))
print(f'Números Pares: {listaNumPares}')
print(f'Números Impares: {listaNumImpares}')