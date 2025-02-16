numeros = [1,2,5,4,3]
letras = ['B', 'C', 'A', 'E', 'D']

print(f'Mezcla de Listas, sin Orden: {list(zip(numeros, letras))}')
print(f'Mezcla de Listas, con Orden Númerico: {sorted(zip(numeros, letras))}')
print(f'Mezcla de Listas, con Orden Alfabético: {sorted(zip(letras, numeros))}')
print(f'Mezcla de Listas, con Orden Númerico y Alfabético: {list(zip(sorted(numeros), sorted(letras)))}')