# ¿Cómo procesar Documentos JSON con Python?:
from urllib import request
import json

# Recuperamos la información del archivo JSON de la web
    # Solicitamos la información
jsonPeticion = request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data = None,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
            )
    # Leemos la información solicitada
jsonObjeto = request.urlopen(jsonPeticion)
jsonArchivo = json.load(jsonObjeto)
print(jsonArchivo)

# Imprimimos las llaves y los valores de la información (se visualiza el documento JSON como un diccionario de Python)
for llave, valor in jsonArchivo.items():
    print(f'{llave}: {valor}')

# Imprimimos solamente la información de las personas (dentro del archivo JSON, las personas se visualizan como una
# lista de diccionarios)
for persona in jsonArchivo['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')