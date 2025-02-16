# El alcance (scope de las variables se refiere a los niveles en los cuales la variable puede ser utilizada)

variableGlobal = 1
print(f'Impresión de Variable Global (desde el nivel más alto): {variableGlobal}')

def funcion():
    variableDeFuncion = 2
    global variableGlobal
    print(f'Impresión de Variable Global (desde el nivel medio): {variableGlobal}')
    print(f'Impresión de Variable de Función (desde el nivel medio): {variableDeFuncion}')
    variableGlobal = 1 # <-- Esta línea código hace que el compilador piense que queremos redefinir la VariableGlobal
                       # localmente, por lo que la linea 9 de este programa regresa un error, ya que estamos usando
                       # una variable que todavía no se define. Para resolver esto, debemos implementar la línea 8
    def funcionDentroDeFuncion():
        variableDeFuncionDeFuncion = 3
        print(f'Impresión de Variable Global (desde el nivel más bajo): {variableGlobal}')
        print(f'Impresión de Variable de Función (desde el nivel más bajo): {variableDeFuncion}')
        print(f'Impresión de Variable de Función de Función (desde el nivel más bajo): {variableDeFuncionDeFuncion}')
    funcionDentroDeFuncion()

funcion()
