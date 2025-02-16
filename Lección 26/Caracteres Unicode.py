# Impresion de Caracteres Unicode

    # Impresión del caracter ' ' en una oración
print(f'Hola\u0020Mundo')

    # Impresión de la letra A con distintas notaciones
print(f'A - notación simple:', '\u0041')
print(f'A - notación extendida:', '\U00000041')
print(f'A - notación hexadecimal:', '\x41') # <-- Esta notación solo registra 2 digitos hexadecimales