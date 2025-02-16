import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        pass
        with conexion.cursor() as cursor:
            cSentencia = 'INSERT INTO persona(cnombre, capellido, cmail) VALUES(%s, %s, %s)'
            cValores = ('Andres', 'Alvarez', 'andres@gmail.com')
            cursor.execute(cSentencia, cValores)
            # NOTA: Cuando ejecutamos un cambio a la base de datos y no usemos la sintaxis de WITH <conexion>, debemos guardar el cambio
            # conexion.commit()
            iRegistrosCreados = cursor.rowcount
            print(f'# de Registros Creados: {iRegistrosCreados}')
except BaseException as e:
    print(f'ERROR: No se pudo establecer una conexion con la base de datos')
else:
    print(f'La conexion con la base de datos fue exitosa')