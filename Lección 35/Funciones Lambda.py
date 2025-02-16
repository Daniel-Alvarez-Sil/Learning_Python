# Las Funciones Lambda son funciones sin nombre y muy cortas en longitud

# Ejemplos de función Lambda:
# Sintáxis:     lambda <parametros>: <valor de retorno>

funcionLambda = lambda a, b: a + b
print(f'La suma de 5 y 4 es {funcionLambda(5, 4)}')

funcionLambda2 = lambda: 'Función Lambda sin Argumentos'
print(f'Mensaje de la función: {funcionLambda2()}')

funcionLambdaConParametrosDefault = lambda a = 0, b = 5: a + b
print(f'La suma de 0 y 5 es {funcionLambdaConParametrosDefault()}')
print(f'La suma de 4 y 10 es {funcionLambdaConParametrosDefault(4, 10)}')

funcionLambdaConParametrosAsterisk = lambda *args, **kwargs: len(args) + len(kwargs)
llaves = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(f'La suma de las longitudes de la tupla, {tuple(range(1,6))}, y del diccionario, {dict(zip(llaves, list(range(1,11))))}, es {funcionLambdaConParametrosAsterisk(*tuple(range(1,6)), **dict(zip(llaves, list(range(1,11)))))}')


# Área de Pruebas
# def funcionPruebaAsterisk(*args):
#     print(type(args))
#     print(args)
#     for arg in args:
#         print(type(arg))
#         print(arg)
#
# lista = [1,2,3,3.5,4]
# tupla = (1,2,3,4,5)
# funcionPruebaAsterisk(*tupla)