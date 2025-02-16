# Este Módulo se encarga de crear un objeto que ejecute las funciones CRUD sobre la base de datos

from Modulo_de_Log import log
from Modulo_de_Cursor_de_Conexion_de_Pool import Cursor
from Modulo_de_Usuario import Usuario


class UsuarioDAO:
# Atributos estáticos
    # CREATE:
    cINSERT = 'INSERT INTO usuario(cuser, cpassword) VALUES(%s, %s)'
    # READ:
    cSELECT = 'SELECT * FROM usuario ORDER BY iid'
    # UPDATE:
    cUPDATE = 'UPDATE usuario SET cuser = %s, cpassword = %s WHERE iid = %s'
    # DELETE:
    cDELETE = 'DELETE FROM usuario WHERE iid = %s'

# Métodos estáticos
    # Create:
    @classmethod
    def insert(cls, oParamUsuario):
        with Cursor() as cursor:
            tParametros = (oParamUsuario.cUser, oParamUsuario.cPassword)
            log.info(f'Inicio de Creación de Usuario. ')
            log.debug(f'Información del usuario a crear: {tParametros}.')
            cursor.execute(cls.cINSERT, tParametros)
            if cursor.rowcount >= 1:
                log.info(f'El usuario ha sido creado exitosamente. ')
            else:
                log.error(f'El usuario no pudo ser creado. Por favor valida tu información e intenta nuevamente. ')
            return cursor.rowcount

    # Read:
    @classmethod
    def select(cls):
        with Cursor() as cursor:
            log.info(f'Inicio de Consulta de Usuarios.')
            cursor.execute(cls.cSELECT)
            registros = cursor.fetchall()
            outputConsulta = []
            if len(registros) >= 1:
                for registro in registros:
                    log.debug(f'{registro}')
                    usuario = Usuario(registro[0], registro[1], registro[2])
                    outputConsulta.append(usuario)
            else:
                log.error(f'No hay registros por leer. ')
            log.info(f'Se ha terminado de ejecutar la lectura de la base de datos. ')
            return outputConsulta

    # Update:
    @classmethod
    def update(cls, oParamUsuario):
        with Cursor() as cursor:
            tParametros = (oParamUsuario.cUser, oParamUsuario.cPassword, oParamUsuario.iID)
            log.info(f'Inicio de Actualización del Usuario #{oParamUsuario.iID}. ')
            cursor.execute(cls.cUPDATE, tParametros)
            log.debug(f'Información de la actualización: {tParametros}. ')
            if cursor.rowcount >= 1:
                log.info(f'El usuario ha sido actualizada exitosamente. ')
            else:
                log.error(f'El usuario no pudo ser actualizado. Por favor valida tu información e intenta nuevamente. ')
            return cursor.rowcount

    # Delete:
    @classmethod
    def delete(cls, oParamUsuario):
        with Cursor() as cursor:
            tParametros = (oParamUsuario.iID,)
            log.info(f'Inicio de Eliminación del Usuario #{oParamUsuario.iID}. ')
            cursor.execute(cls.cDELETE, tParametros)
            if cursor.rowcount >= 1:
                log.info(f'El usuario se ha eliminado correctamente. ')
            else:
                log.error(f'El usuario no ha podido ser eliminado. Por favor valida tu información e intenta nuevamente. ')
            return cursor.rowcount


if __name__ != '__main__':
    log.info(f'{__name__} ha sido importado con éxito. ')
else:
    # Prueba de Create:
    usuario1 = Usuario(None, "User3", "45678")
    UsuarioDAO.insert(usuario1)

    # Prueba de Read:
    consulta = UsuarioDAO.select()

    # Prueba de Update:
    usuario1 = Usuario(7, "User7", "09876")
    UsuarioDAO.update(usuario1)

    # Prueba de Update:
    usuario1 = Usuario(iParamID = 11)
    UsuarioDAO.delete(usuario1)
