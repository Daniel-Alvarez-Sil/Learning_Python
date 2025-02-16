# Herencia Simple

# Clase Padre
class ListaSimple(object):
    def __init__(self, listParamElementos):
        self._elementos = list(listParamElementos)

    @property
    def elementos(self):
        return self._elementos

    @elementos.setter
    def elementos(self, listParamElementos):
        self._elementos = listParamElementos

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elementos!r})'

    def __getitem__(self, iIndice):
        return self.elementos[iIndice]

    def agregar(self, iParamElemento):
        self.elementos.append(iParamElemento)

    def ordenar(self):
        self.elementos.sort()

# Clases Hijas
class ListaOrdenada(ListaSimple):
    def __init__(self, listParamElementos = []):
        super().__init__(listParamElementos)
        super().ordenar()

    def agregar(self, iParamElemento):
        super().agregar(iParamElemento)
        super().ordenar()

class ListaSoloEnteros(ListaSimple):
    def __init__(self, listParamElementos = []):
        listAuxiliar = []
        [listAuxiliar.append(elemento) for elemento in listParamElementos if isinstance(elemento, int)]
        super().__init__(listAuxiliar)

    def agregar(self, iParamElemento):
        if isinstance(iParamElemento, int):
            super().agregar(iParamElemento)

if __name__ != '__main__':
    print(f'Los módulos de herencia simple han sido importados correctamente. ')
else:
    # Lista Padre
    lista1 = ListaSimple([1,2,3,4])
    print(lista1.elementos)
    print(lista1)
    # Listas Hijas
    listaOrdenada1 = ListaOrdenada((5,10,9,0,0.1))
    print(listaOrdenada1.elementos)
    print(listaOrdenada1)
    listaOrdenada1.agregar(6)
    print(listaOrdenada1.elementos)
    print(listaOrdenada1)

    listaSoloEnteros1 = ListaSoloEnteros((1,2,3,'aaaa'))
    print(listaSoloEnteros1.elementos)
    print(listaSoloEnteros1)
    listaSoloEnteros1.agregar(10)
    print(listaSoloEnteros1.elementos)
    print(listaSoloEnteros1)