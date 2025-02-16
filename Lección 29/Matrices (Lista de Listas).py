matriz = [[1,2,3], [4,5,6], [7,8,9,10]]

print(f'Matriz Original: {matriz}')

print(f'Renglón 1, Columna 2: {matriz[1][2]}')
print(f'Renglón 2, Columna 3: {matriz[2][3]}')

matriz[2][3] = 1000
print(f'Matriz Modificada: {matriz}')

