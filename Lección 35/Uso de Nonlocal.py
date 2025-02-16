# Nonlocal es una función que especifica que se debe usar una variable definida a un nivel más externo
# Ejemplo:

def funcion():
    variableDeFuncion = 1
    print(f'Impresión de la Variable de Función (a un nivel intermedio): {variableDeFuncion}')
    def funcionDeFuncion():
        nonlocal variableDeFuncion # <-- Esta sintáxis indica que queremos trabajar con la variable definida en el nivel
        variableDeFuncion = 2      #     exterior, por lo que estaremos trabajando directamente con la variable no local
    funcionDeFuncion()
    print(f'Impresión de la Variable de Función (a un nivel intermedio): {variableDeFuncion}')

funcion()