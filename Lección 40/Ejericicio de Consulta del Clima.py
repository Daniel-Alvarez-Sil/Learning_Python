# Consulta del Clima

from urllib import request
import json

# Asignamos la url del documento JSON
cURL = 'http://globalmentoring.com.mx/api/clima.json'

# Recuperamos la información del archivo JSON
    # Creamos una petición por la información
jsonPeticion = request.Request(
    cURL,
    data = None,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
    # Obtenemos el objeto HTTP solicitado
jsonObjeto = request.urlopen(jsonPeticion)
    # Obtenemos el archivo JSON requerido
jsonArchivo = json.load(jsonObjeto)

# Método recursivo para extraer la información de un documento JSON
def extraerInfoJSON(llave = '', valor = ''):
    if isinstance(valor, list) or isinstance(valor, dict):
        for elemento in valor:
            if not isinstance(elemento, dict):
                extraerInfoJSON(elemento, valor[elemento])
            else:
                extraerInfoJSON(valor = elemento)
    else:
        print(f'{llave}: {valor}')

# Imprimimos la información de manera sistemática
for llave, valor in jsonArchivo.items():
    print(llave.center((30 - len(llave)) + len(llave), '+'))
    extraerInfoJSON(llave, valor)