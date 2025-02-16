import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        pass
        with conexion.cursor() as cursor:
            cSentencia = 'DELETE FROM persona WHERE iid = %s'
            cParametros = (8,)
            cursor.execute(cSentencia, cParametros)
            print(f'# de Registros Eliminados: {cursor.rowcount}')
except BaseException as e:
    print(f'ERROR: Dany, hay un error en tu código\nDetalle del error: {e}')
else:
    print(f'La conexion con la base de datos fue exitosa')
    conexion.close()