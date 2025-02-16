import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        pass
        with conexion.cursor() as cursor:
            cSentencia = "UPDATE persona SET cnombre = %s, cmail = %s WHERE iid = %s"
            cParametros = ('Anastasio', 'anagomez@gmail.com', 8)
            cursor.execute(cSentencia, cParametros)
            print(f'# de Registros Actualizados: {cursor.rowcount}')
except BaseException as e:
    print(f'ERROR: Dany, hay un error en tu código\nDetlle del error: {e}')
else:
    print(f'La conexion con la base de datos fue exitosa')
    conexion.close()