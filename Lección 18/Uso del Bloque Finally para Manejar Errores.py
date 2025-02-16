fResultado = None

try:
    iA = int(input("Ingresa el numero entero A: "))
    iB = int(input("Ingresa el numero entero B: "))
    fResultado = iA/iB

except BaseException as e:
    print(f'ERROR: La operación no se pudo concretar por el siguiente error --> {e}')
else:
    print(f'El resultado de {iA}/{iB} es {fResultado:.2f}')
#Bloque FINALLY: este bloque se ejecuta no importa si hubo algun error o no
finally:
    print("Fin del Programa". center(25, ' '))