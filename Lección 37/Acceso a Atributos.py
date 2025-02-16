# Acceso a Atributos
# Es importante recordar que en Python no existe una manera real de modificar el acceso a un atributo
# Sin embargo, mediante el uso de cierta nomenclatura podemos establecer las reglas de acceso para los atributos
# No obstantes, estas reglas son simplemente una convención para el uso de programadores, y no constituyen reglas reales

class MiClase:
    def __init__(self, cParamPublico, cParamProtegido, cParamPrivado):
        # Atributo Público
        # Este atributo puede ser modificado desde cualquier parte del programa
        self.cPublico = cParamPublico
        # Atributo Protegido
        # Este atributo solo debe ser accedido dentro de la misma clase o clases hijas
        self._cProtegido = cParamProtegido
        # Atributo Privado
        # Este atributo solo debe ser accedido dentro de la misma clase
        self.__cPrivado = cParamPrivado

clase1 = MiClase('Valor Público', 'Valor Protegido', 'Valor Privado')

# Acceso a los distintos tipos de atributos
    # Atributo Público
print(f'Accesando al atributo público: {clase1.cPublico}')
clase1.cPublico = 'Nuevo Valor Público'
print(f'Modificación del atributo público: {clase1.cPublico}')
    # Atributo Protegido
print(f'Accesando al atributo protegido: {clase1._cProtegido}')
clase1._cProtegido = 'Nuevo Valor Protegido'
print(f'Modificación del atributo protegido: {clase1._cProtegido}')
    # Atributo Privado
print(f'Accesando al atributo privado: {clase1._MiClase__cPrivado}')
clase1._MiClase__cPrivado = 'Nuevo Valor Privado'
print(f'Modificación del atributo privado: {clase1._MiClase__cPrivado}')


