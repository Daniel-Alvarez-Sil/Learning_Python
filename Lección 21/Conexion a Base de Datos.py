import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    database = 'test_db',)

# Creamos una variabla que almacene un CURSOR
# La funcion de CURSOR nos permite ejecutar sentencias de SQL

cursor = conexion.cursor()
sentenciaSQL = 'SELECT * FROM persona'
cursor.execute(sentenciaSQL)
registros = cursor.fetchall()
print(registros)
