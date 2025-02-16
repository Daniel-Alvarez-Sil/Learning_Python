# Un Generador Anónimo (expresión generadora) es una función sin nombre que constituye una sola línea de código,
# pero que cumple con las funciones de un generador

# Ejemplo:

# Sintáxis:  (<valores a returnar (yield)> for <expresión iterable>)
exponentes = (valor*valor for valor in range(11))
# Esta línea de código es igual a esto:
def funcionGeneradora():
    for valor in range(11):
        yield valor*valor

print(f'Referencia de la expresión generadora: {exponentes}')
print(f'Impresión de los Valores de la Secuencia del Generador: ')
for exponente in exponentes:
    print(f'Valor: {exponente}')

# El uso de una expresión generadora como parámetro en una función
suma = sum(valor*valor for valor in range(11)) # <-- Como ya hemos consumido el generador, debemos volver a definir la
                                               #     expresión generadora
print(f'La suma de los valores de la secuencia es: {suma}')

