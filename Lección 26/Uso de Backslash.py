# Distintos Usos de Backslash

    # Backslash como escape
cString = 'Caracteres de comillas: \' \' '
print(f'{cString}')

    # Eliminación de caracteres mediante el comando \b
cString = 'Se va a eliminar el punto.\b'
print(f'{cString}')

    # Formas de utilizar backslash
cString = 'C:\\nueva carpeta\\noel'
print(f'{cString}')
rawString = r'C:\nueva carpeta\noel' # <-- Esto es un raw string
print(f'{cString}')