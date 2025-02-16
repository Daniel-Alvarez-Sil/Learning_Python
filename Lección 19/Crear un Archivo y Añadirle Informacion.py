#docCopia = None
#docArchivo = None

try:
    docCopia = open("copia_de_prueba.txt", "a", encoding="utf8")
except BaseException as e:
    print(f'ERROR: El documento ingresado no ha podido ser abierto por el siguiente error --> {e}')
else:
    try:
        docArchivo = open("prueba.txt", "r", encoding="utf8")
    except BaseException as e:
        print(f'ERROR: El documento ingresado no ha podido ser abierto por el siguiente error --> {e}')
    else:
        docCopia.write(docArchivo.read())
        docArchivo.close()
        docCopia.close()
finally:
    print("Fin del Programa". center(80, '-'))