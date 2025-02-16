import psycopg2

try:
    with psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db') as conexion:
        pass
        with conexion.cursor() as cursor:
            cSentencia = 'SELECT * FROM persona WHERE persona.iid IN %s'
            entradaTuplas = input("Ingresa los ID´s (separados por comas) de las personas que deseas buscar: ")
            tuplaParametro = (tuple(entradaTuplas.split(',')),)
            cursor.execute(cSentencia, tuplaParametro)
            resultados = (None,)
            resultados = cursor.fetchall()

            print(f'Resultado de la ejecución: ')

            if resultados == []:
                print("No hay resultados para la busqueda ingresada")
            else:
                for resultado in resultados:
                    print(f'{resultado}')
except BaseException as e:
    print(f'ERROR: No se pudo completar la conexion a la base de datos por el siguiente error --> {e}')
else:
    print(f'La conexion a la base de datos, {conexion}, fue exitosa')
    conexion.close()
