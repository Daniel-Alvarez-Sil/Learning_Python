# Módulo para crear objetos de tipo Usuario que correspondan a los registros de la base de datos

from Modulo_de_Log import log

class Usuario:
    # Método para definir los atributos de cada instancia de la clase
    def __init__(self, iParamID = None, cParamUser = None, cParamPassword = None):
        self._iID = iParamID
        self._cUser = cParamUser
        self._cPassword = cParamPassword

# iID
    # Método GET
    @property
    def iID(self):
        return self._iID
    # Método SET
    @iID.setter
    def iID(self, iParamID):
        self._iID = iParamID

# cUser
    # Método GET
    @property
    def cUser(self):
        return self._cUser
    #Método SET
    @cUser.setter
    def cUser(self, cParamUser):
        self._cUser = cParamUser

# cPassword
    # Método GET
    @property
    def cPassword(self):
        return self._cPassword
    # Método SET
    @cPassword.setter
    def cPassword(self, cParamPassword):
        self._cPassword = cParamPassword

    # Método para imprimir los atributos de la instancia de la clase
    def __str__(self):
        return f'Usuario #{self._iID} --> User: {self._cUser}, Password = {self._cPassword}'

if __name__ != '__main__':
    log.info(f'{__name__} ha sido importado con éxito')
else:
    usuario1 = Usuario(cParamUser = 'User1', cParamPassword = '1234')
    log.info(usuario1)