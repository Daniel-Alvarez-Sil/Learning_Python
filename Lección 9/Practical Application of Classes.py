import random

class Disciples():
    def __init__(self, Nombre, Id, Give, Reciever, Reciever2):
        self.cNombre = Nombre
        self.iID = Id
        self.lGive = Give
        self.iReciever = Reciever
        self.cReciever = Reciever2

i = int(input("Ingresa el número de participantes en el Intercambio: "))
disciple = [Disciples("", x, False, -1, "") for x in range(i)]

for object in disciple:
    object.cNombre = input("Ingresa el nombre del participante: ")

auxDisciple = disciple

for object2 in disciple:
    auxObject = random.choice(auxDisciple)
    while auxObject.iID == object2.iID or auxObject.lGive == True:
            auxObject = random.choice(auxDisciple)
    object2.iReciever = auxObject.iID
    object2.cReciever = auxObject.cNombre
    auxObject.lGive = True


print(f'Resultados del Intercambio:')

for object3 in disciple:
    print(f'{object3.cNombre} le da a {object3.cReciever}')

