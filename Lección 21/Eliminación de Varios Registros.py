import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        pass
        with conexion.cursor() as cursor:
            cSentencia = 'DELETE FROM persona WHERE iid IN %s'
            # NOTA: Creación de una tupla de tuplas de parametros
            cParametros = (tuple(input("Ingresa el ID de las personas que deseas eliminar (separados por comas): ").split(',')),)
            cursor.execute(cSentencia, cParametros)
            print(f'# de Registros Eliminados: {cursor.rowcount}')
except BaseException as e:
    print(f'ERROR: Dany, hay un error en tu código\nDetalle del error: {e}')
else:
    print(f'La conexion con la base de datos fue exitosa')
    conexion.close()