from Modulo_de_Excepcion_Personalizada import EqualValuesException

fResultado = None

try:
    iA = int(input("Ingresa el numero entero A: "))
    iB = int(input("Ingresa el numero entero B: "))
    fResultado = iA/iB
    #Llamamos nuestra excepcion personalizada mediante la funcion RAISE
    if iA == iB:
        raise EqualValuesException('Los dos numeros ingresados no pueden ser iguales')
except BaseException as e:
    print(f'ERROR: La operacion no pudo ser concretada por el siguiente error --> {e}')
else:
    print(f'El resultado de la operacion {iA}/{iB} es {fResultado}')
finally:
    print("Fin del programa". center(75, '-'))