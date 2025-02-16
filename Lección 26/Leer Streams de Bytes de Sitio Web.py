# Este programa lee información de un sitio web

    # Importamos 2 clases que serán necesarias
from urllib.request import urlopen
from urllib.request import Request

    # Definimos la URL como una REQUEST y procedemos a añadir HEADERS
cURL = Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
cURL.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')

    # Usamos un resource manager para abrir el archivo
with urlopen(cURL) as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

    # Procedemos a imprimir la información del sitio WEB en un documento TXT
with open('Información de Sitio WEB.txt', 'w', encoding = 'utf-8') as archivo:
    archivo.write(contenido)
        # NOTA: archivo.close() <-- Recordemos que los Resource Managers cierran automaticamente su Resource correspondiente

    # Rescatamos cada palabra del sitio WEB y las asignamos a una lista
palabras = []
with urlopen(cURL) as archivo:
    for linea in archivo:
        palabrasEnLinea = linea.decode('utf-8').split()
        for palabra in palabrasEnLinea:
            palabras.append(palabra)

print(palabras)

