try:
    docArchivo = open("prueba.txt", "w", encoding="utf8")
except BaseException as e:
    print(f'ERROR: No se ha podido abrir el archivo ingresado por el error --> {e}')
else:
    print(f'El archivo, {docArchivo.name}, ha sido abierto correctamente')
    docArchivo.write("Hola, esta es un prueba de escritura\n")
    docArchivo.write("Fin de la Prueba")
    docArchivo.write("\nPrueba de Acentos: áéíóú")
    docArchivo.close()
finally:
    print("Fin del Programa". center(50, "-"))