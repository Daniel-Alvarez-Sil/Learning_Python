# Decoradores
# Un decorador es una función que recibe una función y regresa otra
# Los decoradores se utilizan para extender funcionalidad
# Función Decoradora (A)
# Función a Decorar (B)
# Función Decorada (C)

# Ejemplo abstracto de lo establecido previamente
def A(B):
    def C():
        B()
        print(f'Desde la Función A')
    return C

# NOTA: El código de arriba es lo que pasa detrás de cámaras cuando se ejecuta el código de abajo
@A
def B():
    print(f'Función B')
# Llamamos a la función decorada, C
B()