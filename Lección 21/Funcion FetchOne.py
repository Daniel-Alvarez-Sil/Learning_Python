import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        with conexion.cursor() as cursor:
            # NOTA: Aunque el id de la persona es de tipo entero, la sentencia puede leer este id como si fuese un string
            sentencia = 'SELECT * FROM persona WHERE iid = %s'
            cInputID = input("Ingresa el ID de la persona que deseas consultar: ")
            # NOTA: Cuando la sentencia que queramos ejecutar incluye PLACEHOLDERS, debemos pasar como un parametro una tupla de Variables que correspondan con los PLACEHOLDERS
            cursor.execute(sentencia, (cInputID,))
            resultado = cursor.fetchone()
            print(f'Resultado de la búsqueda: {resultado}')
except Exception as e:
    print(f'ERROR: No se pudo conectar a la base de datos por el siguiente error --> {e} <--')
else:
    conexion.close()