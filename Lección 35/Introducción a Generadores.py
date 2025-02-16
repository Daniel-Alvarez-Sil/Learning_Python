# Los generadores son funciones especiales de Python, las cuales son usadas para generar secuencias
# El comando, yield, es característico de estas funciones, ya que este comando sirve para obtener
# un numero de la secuencia y terminar la ejecución de la función

# Ejemplo:

def generador():
    yield 1
    yield 2
    yield 3

# Pasar la referencia de la función a una variable
print(f'Asignación de la Referencia de la Función Generadora')
gen = generador
print(gen)
print(next(gen()))

print()

# Crear un objeto de la función generadora
print(f'Creación del Objeto Generador')
gen = generador()
print(gen)
print(next(gen))

print()

# Iteración de la secuencia de un generador
print(f'Impresión de la Secuencia Completa')
for gen in generador():
    print(gen)

