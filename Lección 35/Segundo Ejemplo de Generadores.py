# Generador de Numeros del 1 al 5
def generador():
    for numero in range(1,6):
        yield numero
        print(f'Se reanuda la ejecución. (Número Actual = {numero})')

gen = generador()
print(f'Impresión de la Secuencia del Generador: ')
for valor in gen:
    print(valor)

print()

# Si queremos volver a imprimir la secuencia, debemos reiniciar el generador
gen = generador()
print(f'2da Impresión de la Secuencia del Generador: ')
for valor in gen:
    print(valor)

print()

# Consumación de un generador por medio de un ciclo while
gen = generador()
print(f'Impresión de la Secuencia del Generador Usando un Ciclo While: ')
while True:
    try:
        valor = next(gen)
        print(valor)
    except BaseException:
        print(f'Se ha terminado de iterar el generador. ')
        break # <-- Si no usamos este comando, la función se repite infinitamente

