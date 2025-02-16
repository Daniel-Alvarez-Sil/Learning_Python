# Ejemplo:

def funcionDecoradora(funcionADecorar):
    def funcionDecorada(*valoresASumar): # <-- Los parámetros pasados a la función decorada corresponden a los parámetros de la función a decorar
        print(f'Cargando...')
        return funcionADecorar(*valoresASumar)
    return funcionDecorada

@funcionDecoradora
def suma(a, b):
    return a + b

print(f'La suma de 4.5 y 6.7 es {suma(4.5, 6.7)}')