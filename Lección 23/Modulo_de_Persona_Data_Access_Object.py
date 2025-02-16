from Modulo_de_Persona import Persona
from Modulo_de_Cursor_de_Conexion_de_Pool import Cursor
from Modulo_de_Log import log

class PersonaDAO:
    #Create:
    cINSERT = 'INSERT INTO persona(cnombre, capellido, cmail) VALUES(%s, %s, %s)'

    @classmethod
    def insert(cls, oParamPersona):
        tParametros = (oParamPersona.cNombre, oParamPersona.cApellido, oParamPersona.cMail)
        with Cursor() as cursor:
            cursor.execute(cls.cINSERT, tParametros)
            log.debug(f'Se ha creado la siguiente persona: {oParamPersona}')
            return cursor.rowcount

    #Read:
    cSELECT = 'SELECT * FROM persona ORDER BY iid'

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            log.debug(f'Impresión de los registros de la base de datos: ')
            cursor.execute(cls.cSELECT)
            #print(f'Registros: ')
            lConsulta = []
            for registro in cursor.fetchall():
                log.debug(registro)
                lConsulta.append(registro)
            return lConsulta


    #Update:
    cUPDATE = 'UPDATE persona SET cnombre = %s, capellido = %s, cmail = %s WHERE iiD = %s'

    @classmethod
    def update(cls, oParamPersona):
        with Cursor() as cursor:
            tParametros = (oParamPersona.cNombre, oParamPersona.cApellido, oParamPersona.cMail, oParamPersona.iID)
            cursor.execute(cls.cUPDATE, tParametros)
            log.debug(f'Se ha actualizado a la siguiente persona: {oParamPersona}')
            return cursor.rowcount

    #Delete:
    cDELETE = 'DELETE FROM persona WHERE iid = %s'

    @classmethod
    def delete(cls, oParamPersona):
        with Cursor() as cursor:
            tParametros = (oParamPersona.iID,)
            cursor.execute(cls.cDELETE, tParametros)
            log.debug(f'Se ha eliminado a la siguiente persona: {oParamPersona}')
            return cursor.rowcount


if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    pass
    #Prueba de Create:
    #persona1 = Persona(None, "Damian", "Wayne", "dwayne@mail.com")
    #PersonaDAO.insert(persona1)

    #Prueba de Read:
    #PersonaDAO.select()

    #Prueba de Update:
    #persona1 = Persona(20, "Alicia", "Lopez", "alopez@gmail.com")
    #PersonaDAO.update(persona1)

    #Prueba de Delete:
    #persona1 = Persona(iParamID = 17)
    #PersonaDAO.delete(persona1)