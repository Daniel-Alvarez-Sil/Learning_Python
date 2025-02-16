from dataclasses import dataclass
from typing import ClassVar

# El decorador, dataclass, sirve para añadir funcionalidad dinámicamente a una clase
# Este decorador agrega funciones que no se han sobreescrito como __init__, etc..
# Es recomendable solo usar este decorador con clases pequeñas y que requieran poca personalización

# Creación de una clase que será atributo de la clase posterios:
@dataclass(frozen = True)
class Domicilio():
    cCalle: str = ''
    cNumero: str = ''

@dataclass(frozen = True) # <-- Solicitamos al decorador que requerimos que los atributos de la clasea sean inmutables
class Persona(object):
    # Definición de atributos de instancia, cuando se usa el decorador dataclass
    cNombre : str
    cApellido : str = ''
    domDomicilio: Domicilio = Domicilio()

    # Definición de atributos de clase, cuando se usa el decorador dataclass
    CONTADOR_GLOBAL: ClassVar[int] = 0

    # Creación de Validaciones para los Atributos
    def __post_init__(self):
        if not self.cNombre:
            raise ValueError(f'El atributo cNombre de la clase, {self.__class__.__name__}, no puede ser nulo. ')


print(f'Variable Global (Atributo de Instancia): {Persona.CONTADOR_GLOBAL}')
persona1 = Persona('Daniel', 'Alvarez', Domicilio('Cerezos', '3'))
persona2 = Persona('Mariana')
print(f'Persona 1: {persona1}')
print(f'Persona 2: {persona2}')

# Como, con ayuda del decorador dataclass, hemos creado objetos con atributos inmutables, podemos crear un SET:
set = {persona1, persona2}
print(f'Conjunto de instancias inmutables: {set}')

# El decorador dataclass sobreescribe dinámicamente la función __eq__, por lo que podemos hacer lo siguiente:
persona3 = Persona('Mariana')
if persona2 == persona3:
    print(f'La persona 2, {persona2}, y la persona 3, {persona3}, son iguales. ')

