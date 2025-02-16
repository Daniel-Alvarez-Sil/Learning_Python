from Modulo_de_Conexion import Conexion
from Modulo_de_Persona  import Persona
from Modulo_de_Log      import log

# DAO = Data Access Object

class PersonaDAO:
    # CRUD = Create, Read, Update, and Delete
    # Create:
    cINSERT = 'INSERT INTO persona(cnombre, capellido, cmail) VALUES(%s, %s, %s)'
    # Read:
    cSELECT = 'SELECT * FROM persona ORDER BY iid'
    # Update
    cUPDATE = 'UPDATE persona SET cnombre = %s, capellido = %s, cmail = %s WHERE iid = %s'
    # Delete
    cDELETE = 'DELETE FROM persona WHERE iid = %s'

    # Create:
    @classmethod
    def insert(cls, oParamPersona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                lParametros = (oParamPersona.cNombre, oParamPersona.cApellido, oParamPersona.cMail)
                cursor.execute(cls.cINSERT, lParametros)
                log.debug(f'Persona Insertada: {oParamPersona}')
                #log.debug(f' Cursor abierto: {cursor.closed}')
                return cursor.rowcount

    @classmethod
    # Read:
    def select(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls.cSELECT)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    # Update:
    @classmethod
    def update(cls, oParamPersona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                lParametros = (oParamPersona.cNombre, oParamPersona.cApellido, oParamPersona.cMail, oParamPersona.iID)
                cursor.execute(cls.cUPDATE, lParametros)
                log.debug(f'Persona Actualizada: {oParamPersona}')
                return cursor.rowcount

    # Delete
    @classmethod
    def delete(cls, oParamPersona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                lParametros = (oParamPersona.iID, )
                cursor.execute(cls.cDELETE, lParametros)
                log.debug(f'Persona Eliminada: {oParamPersona}')
                return cursor.rowcount

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    # Prueba de CREATE
    persona = Persona(cParamNombre = input("Ingresa el nombre de la persona a ingresar: "), cParamApellido = input("Ingresa el apellido de la persona a ingresar: "), cParamMail = input("Ingresa el correo de la persona a ingresar: "))
    iRows = PersonaDAO.insert(persona)
    log.debug(f'Numero de Registros Creados: {iRows}')

    #log.debug(f'Cursor cerrado: {Conexion.obtenerCursor().closed}')

    # Prueba de READ
    consulta = PersonaDAO.select()
    for registro in consulta:
        log.debug(registro)

    # Prueba de UPDATE
    persona = Persona(iParamID = input("Ingresa el ID de la persona a modificar: "))
    iRows = PersonaDAO.update(persona)
    log.debug(f'Numero de Registros Actualizados: {iRows}')

    # Prueba de DELETE
    persona = Persona(iParamID = input("Ingresa el ID de la persona a eliminar: "))
    iRows = PersonaDAO.delete(persona)
    log.debug(f'Numero de Registros Eliminados: {iRows}')