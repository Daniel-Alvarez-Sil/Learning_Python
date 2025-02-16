docArchivo = None

try:
    docArchivo = open('prueba.txt', "r", encoding="utf8")
except BaseException as e:
    print(f'ERROR: El documento ingresado no se ha podido abrir debido al siguiente error --> {e}')
else:
    print(f'El documento, {docArchivo.name}, ha sido abierto con exito')
    #Para leer todo el documento
    #print(docArchivo.read())

    #Para Leer solo unos caracteres del Documento
    #print(docArchivo.read(5))
    #print(docArchivo.read(5))

    #Para leer 1 linea completa
    #print(docArchivo.readline())

    #Para iterar las lineas del archivo
    #for linea in docArchivo:
    #    print(linea)

    #Leer todas las lineas del archivo
    #print(docArchivo.readlines())

    #Acceder a una Linea Especifica de la Lista
    print(docArchivo.readlines()[2])

    docArchivo.close()
finally:
    print(f'Fin del Programa'. center(80, '-'))
