from Ejemplo_de_Herencia_Simple import *

class ListaSoloEnterosOrdenados(ListaSoloEnteros, ListaOrdenada):
    pass

listaSoloEnterosOrdenados1 = ListaSoloEnterosOrdenados((9,1.1,10,11,6,5,2,3))
# NOTA: En cuantos a los métodos heredados y sobreescritos concierne, los métodos que se encuentren más a la izquierda
#       en el MRO, tienen más prioridad
print(f'Orden de la Jerarquía de una Clase con Herencia Múltiple (MRO): {ListaSoloEnterosOrdenados.__mro__}')
print(listaSoloEnterosOrdenados1)