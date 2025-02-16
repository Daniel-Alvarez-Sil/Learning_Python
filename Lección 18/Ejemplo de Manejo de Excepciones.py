resultado = None
a = int(input("Ingresa el numero entero a: "))
b = int(input("Ingresa el numero entero b: "))

try:
    #Si la operacion a/b retorna un error, el valor de la variable resultado se mantiene igual
    resultado = a/b
except BaseException as e:
    print(f'Existe el siguiente error: {e}')
else:
    print(f'El resultado de {a}/{b} es {resultado}')
    print("Continuamos...")