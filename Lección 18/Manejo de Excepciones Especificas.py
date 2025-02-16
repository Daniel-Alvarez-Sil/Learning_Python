iResultado = None

try:
    iA = int(input("Ingresa el entero a: "))
    iB = int(input("Ingresa el entero b: "))
    iResultado = iA/iB

#Cadena de Manejos de Errores en orden de más específico a menos específico
except ZeroDivisionError:
    print("ERROR: No puedes dividir entre 0")
except TypeError:
    print("ERROR: No puedes dividir una variable que no sea de tipo numerica")
except BaseException as e:
    print(f"ERROR: La operacion no fue exitosa. Detalle --> {e}")
#Impresion del resultado, en caso de no haber error
else:
    print(f'El resultado de {iA}/{iB} es {iResultado}')
    print("Continuamos...")