# Unpacking es el nombre que se le asigna, en Python, a el concepto de asignar, de manera simultánea, varios valores a varias variables

# Ejemplo de Asignamiento Normal
print(f'Ejemplo de Asignamiento Normal'.center(len('Ejemplo de Asignamiento Normal') + 8, '+'))

print('\n')

tupla1 = 1,2,3
print(f'Valor de la variable: {tupla1}\nTipo de Dato: {type(tupla1)}')

print('\n')

# Ejemplos de Unpacking
print(f'Ejemplos de Unpacking'.center(len('Ejemplos de Unpacking') + 16, '-'))

print('\n')

valor1, valor2, valor3 = 1, 2, 3
print(f'Valor de las variables: {valor1, valor2, valor3}\nTipos de Datos: {type(valor1), type(valor2), type(valor3)}')

print('\n')

valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8,9
print(f'Valor de las variables: {valor1, valor2, valor3}\nTipos de Datos: {type(valor1), type(valor2), type(valor3)}')

print('\n')

valor1, valor2, *valor3, valor4, valor5 = (1,2,3,4,5,6,7,8,9,10)
print(f'Valores de las variables: {valor1, valor2, valor3, valor4, valor5}\nTipos de Datos: {type(valor1), type(valor2), type(valor3), type(valor4), type(valor5)}')

print('\n')

    # NOTA: El concepto de unpacking funciona tanto con listas como con tuplas

valor1, valor2, *valor3, valor4, valor5 = [1,2,3,4,5,6,7,8,9,10]
print(f'Valores de las variables: {valor1, valor2, valor3, valor4, valor5}\nTipos de Datos: {type(valor1), type(valor2), type(valor3), type(valor4), type(valor5)}')