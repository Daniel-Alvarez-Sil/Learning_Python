import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        with conexion.cursor() as cursor:
            cSentencia = 'INSERT INTO persona(cnombre, capellido, cmail) VALUES(%s, %s, %s)'
            cValues = (
                ("Oswaldo", "Ramirez", "oramirez@gmail.com"),
                ("Juan", "Perez", "jperez@gmail.com"),
                ("Anna", "Gomez", "agomez@gmail.com")
            )
            # Para insertar varios registros a la base de datos, usamos la siguiente sintaxis:
            # cursor.executemany(<sentencia>, <tupla de tuplas de parametros>)
            cursor.executemany(cSentencia, cValues)
            print(f'# de Registros Insertados: {cursor.rowcount}')
except BaseException as e:
    print(f'ERROR: Dany, por favor revisa tu codigo\nDetalle del error: {e}')
else:
    print(f'La conexion a la base de datos fue exitosa')
    conexion.close()