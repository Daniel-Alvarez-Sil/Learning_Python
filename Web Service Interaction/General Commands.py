#Este Programa Explora los Comandos Generales para Interconexión de aplicaciones

#Instalamos e Imprimimos una Libreria Externa
import requests
#URL de API de ejemplo
BASE_URL = "https://fakestoreapi.com"
#Conexión a API para realizar consultas
response = requests.get("https://test.paxfacturacion.com.mx:454/fnEnviarPAX003", auth=("WSDL_PAX", "wqrCssOUw4HDgMSUxJTDq8OkwrQXMnBpSS4Ocm/Cve+/te+9tu++me+/tiEc776v776B"))
#Impresión de Estatus de Transacción, 200 = ÉXITO
print(response.status_code)
