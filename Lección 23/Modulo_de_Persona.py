
class Persona:

    def __init__(self, iParamID = None, cParamNombre = None, cParamApellido = None, cParamMail = None):
        self._iID = iParamID
        self._cNombre = cParamNombre
        self._cApellido = cParamApellido
        self._cMail = cParamMail

# iID:
    #Método GET
    @property
    def iID(self):
        return self._iID
    #Método SET
    @iID.setter
    def iID(self, iParamID):
        self._iID = iParamID

# cNombre:
    #Método GET
    @property
    def cNombre(self):
        return self._cNombre
    #Método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        self._cNombre = cParamNombre

# cApellido:
    #Método GET
    @property
    def cApellido(self):
        return self._cApellido
    #Método SET
    @cApellido.setter
    def cApellido(self, cParamApellido):
        self._cApellido = cParamApellido

# cMail:
    #Método GET
    @property
    def cMail(self):
        return self._cMail
    #Método SET
    @cMail.setter
    def cMail(self, cParamMail):
        self._cMail = cParamMail

# Método para imprimir los atributos de la instancia de la clase
    def __str__(self):
        return f'Persona #{self._iID} --> Nombre: {self._cNombre} {self._cApellido}, Correo: {self._cMail}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    persona1 = Persona(1, "Prueba", "Prueba", "pprueba@mail.com")
    print(persona1)