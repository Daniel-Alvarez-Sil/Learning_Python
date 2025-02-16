# Método REPLACE
print(f'Método REPLACE'.center(30, '-'))

cString = 'Esta es una prueba de reemplazo'
print(f'Cadena original: {cString}. ')
cString = cString.replace(' ', '-')
print(f'Cadena modificada: {cString}. ')

# Método STRIP
# Este método se encarga de eliminar caracteres al prinicipio y al final de una cadena
print(f'Método STRIP'.center(30, '-'))

    # STRIP
cString = ' ***Esta es una prueba de strip*** '
print(f'Cadena original: {cString}, # de caracteres: {len(cString)}')
cString = cString.strip() # <-- Cuando no se especifica ningún caracter entre los parentesis, el método recibe como parametro el caracter ' '
print(f'Cadena modificada: {cString}, # de caracteres: {len(cString)}')

    # Left STRIP
cString = cString.lstrip('*')
print(f'Cadena modificada por el lado izquierda: {cString}')

    # Right STRIP
cString = cString.rstrip('*')
print(f'Cadena modificada por el lado derecho: {cString}')
