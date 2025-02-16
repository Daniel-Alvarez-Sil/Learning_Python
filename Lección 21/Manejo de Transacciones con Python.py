import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = 'admin', host = 'localhost', port = '5432', database = 'test_db')

try:
    # Inicio de Transacción
    conexion.autocommit = False
    cursor = conexion.cursor()

    cSentencia = 'INSERT INTO persona(cnombre, capellido, cmail) VALUES(%s, %s, %s)'
    cParametros = ("Dan", "Acostaaaaaaaaaaaaaaaaaaa", "dacosta@mail.com")
    cursor.execute(cSentencia, cParametros)

    cSentencia = 'UPDATE persona SET cnombre = %s, capellido = %s, cmail = %s WHERE iid = %s'
    cParametros = ('Gabriela Anna', 'Sil', 'gsil@mail.com', 5)
    cursor.execute(cSentencia, cParametros)

    cursor.close()
    # Fin de Transacción
except BaseException as e:
    conexion.rollback()
    print(f'ERROR: Dany, hay un error en tu código\nDetalle del error: {e}')
else:
    conexion.commit()
    print(f'La conexion con la base de datos fue exitosa')
    conexion.close()