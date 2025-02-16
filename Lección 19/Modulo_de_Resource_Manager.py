#En este procedimiento, creamos un objeto para abrir y cerrar recursos usando la funcion WITH

class ResourceManager:
    def __init__(self, recursoParamNombre):
        print("Recibimos el Recurso". center(50, '-'))
        self.recursoNombre = recursoParamNombre

    def __enter__(self):
        print("Abrimos el Recurso". center(50, '-'))
        self.recursoNombre = open(self.recursoNombre, "r", encoding="utf8")
        return self.recursoNombre

    def __exit__(self, cTipoError, cValorError, cTraceback):
        print("Cerramos el Recurso". center(50, '-'))
        if self.recursoNombre: #Validamos que el Objeto esté apuntando a algún recurso
            self.recursoNombre.close()

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')