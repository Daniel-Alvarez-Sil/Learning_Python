import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        pass
        with conexion.cursor() as cursor:
            cSentencia = 'UPDATE persona SET cnombre = %s, capellido = %s, cmail = %s WHERE iid = %s'
            cParametros = (
                ("Lola", "Martinez", "lmartinez@gmail.com", 6),
                ("Gael", "Aguas", "gaguas@gmail.com", 7),
                ("Andres", "alvarado", "aalvarado@gmail.com", 8)
            )
            # Nota para modificar varios registro de la base de datos, utilizamos la siguiente sintaxis:
            # conexion.executemany(<sentencia>, <tupla de tuplas de parametros>)
            cursor.executemany(cSentencia, cParametros)
            print(f'# de Registros Actualizados: {cursor.rowcount}')
except BaseException as e:
    print(f'ERROR: Dany, hay un error en tu código\nDetalle del error: {e}')
else:
    print(f'La conexion con la base de datos fue exitosa')
    conexion.close()