# Usando la funcion "with <resourceManager>(parameters) as <receivingVariable>", no tenemos que hacer lo siguiente
#   - Abrir un archivo (recurso)
#   - Cerrar el archivo (recurso), despues de haberlo abierto
#   - Validar que la apertura del archivo (recurso) haya sido exitosa

from Modulo_de_Resource_Manager import ResourceManager

with ResourceManager("prueba.txt") as docArchivo:
    print(docArchivo.read())


