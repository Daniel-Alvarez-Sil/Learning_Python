# Estudiamos Más Métodos de la Clase STR

cString = 'Esta es una cadena de prueba'
print(f'La cadena original: {cString}')

# Contar el número de ocurrencias de una cadena dentro de una cadena
print(f'El número de veces que la letra \'e\' aparece en la cadena es: {cString.count("e")}')

# Convertir una cadena a letras mayúsculas
print(f'Cadena con letras mayúsculas: {cString.upper()}')

# Consultamos si una cadena tiene todos sus elementos en mayúscula
print(f'¿La cadena anterior tiene todos sus elementos en mayúscula?: {cString.upper().isupper()}')

# Convertir una cadena a letras minúsculas
print(f'Cadena con letras minúsculas: {cString.lower()}')

# Consultamos si una cadena tiene todos sus elementos en minúscula
print(f'¿La cadena anterior tiene todos sus elementos en minúscula?: {cString.lower().islower()}')

# Buscamos una cadena dentro de una cadena
print(f'¿La palabra \'Esta\' aparece en la cadena original?: {"Esta" in cString}')

# Consultamos si una cadena empieza de cierta forma
print(f'¿La cadena comienza con la palabra \'Esta\'?: {cString.startswith("Esta")}')

# Consultamos si una cadena finaliza de cierta forma
print(f'¿La cadena termina con la palbra \'prueba\'?: {cString.endswith("prueba")}')