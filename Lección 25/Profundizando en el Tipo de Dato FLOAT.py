# El constructor de tipo FLOAT, puede leer distintos tipos de datos
fA = float('10')
print(f'Valor flotante: {fA}')
fA = float(10)
print(f'Valor flotante: {fA}')

# Notacion Exponencial, ejemplos:
fA = 3e5 # --> 300,000, NOTA: 3 + 5 ceros
print(f'Valor flotante con notación exponencial, 3e5: {fA}')
fA = 3e-5 # --> 0.00003, NOTA: El numero 3 ocupa la 5ta posición decimal, no la 6ta
print(f'Valor flotante con notación exponencial, 3e-5: {fA:.5f}')

# Cualquier cálculo que involucra un tipo de dato float, es promovido a float
fA = 3.00 + 5
print(f'Valor de la operación, 3.00 + 5: {fA}')