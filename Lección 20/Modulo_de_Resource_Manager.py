class ResourceManager:
    def __init__(self, cParamNombre, cParamModo):
        self.cNombre = cParamNombre
        self.cModo = cParamModo

    def __enter__(self):
        try:
            self.cNombre = open(self.cNombre, self.cModo, encoding="utf8")
        except BaseException:
            self.cNombre = -1
        finally:
            return self.cNombre

    def __exit__(self, cTipoError, cValorError, cTraceback):
        if self.cNombre != -1:
            self.cNombre.close()

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')