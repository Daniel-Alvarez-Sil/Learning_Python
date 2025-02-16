from Modulo_de_Log import log

class Persona:
    def __init__(self, iParamID = None, cParamNombre = None, cParamApellido = None, cParamMail = None):
        self._iID = iParamID
        self._cNombre = cParamNombre
        self._cApellido = cParamApellido
        self._cMail = cParamMail

    #Método GET
    @property
    def iID(self):
        return self._iID
    #Método SET
    @iID.setter
    def iID(self, iParamID):
        self._iID = iParamID

    #Método GET
    @property
    def cNombre(self):
        return self._cNombre
    #Método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        self._cNombre = cParamNombre

    #Método GET
    @property
    def cApellido(self):
        return self._cApellido
    #Método SET
    @cApellido.setter
    def cApellido(self, cParamApellido):
        self._cApellido = cParamApellido

    #Método GET
    @property
    def cMail(self):
        return self._cMail
    #Método SET
    @cMail.setter
    def cMail(self, cParamMail):
        self._cMail = cParamMail

    #Método para imprimir los atributos de la instancia
    def __str__(self):
        return f'Persona #{self._iID} --> Nombre: {self._cNombre} {self._cApellido}, Correo: {self._cMail}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    persona1 = Persona(1, 'Daniel', 'Alvarez', 'dalvarez@mail.com')
    log.debug(persona1)
    # Simular un INSERT
    persona1 = Persona(cParamNombre = 'Daniel', cParamApellido = 'Alvarez', cParamMail = 'dalvarez@mail.com')
    log.debug(persona1)
    # Simular un DELETE
    persona1 = Persona(iParamID = 1)
    log.debug(persona1)