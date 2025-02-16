# Números
    # Número igual a 0.00
number = 0
booVar = bool(number)
print(f'El número, {number}, convertido a tipo bool es {booVar}. ')
    # Número no es igual a 0.00
number = 10
booVar = bool(number)
print(f'El número, {number}, convertido a tipo bool es {booVar}. ')

# Strings
    # Cadena igual a ''
string = ''
booVar = bool(string)
print(f'La cadena, "{string}", convertida a tipo bool es {booVar}. ')
    # Cadena no es igual a ''
string = 'Palabra'
booVar = bool(string)
print(f'La cadena, "{string}", convertida a tipo bool es {booVar}. ')

# Listas (o cualquier tipo de coleccion)
    # Colección vacía
list = []
booVar = bool(list)
print(f'La lista, {list}, convertida a tipo bool es {booVar}. ')
    # Colección no vacía
list = ['Daniel', 'Mariana','Luka']
booVar = bool(list)
print(f'La lista, {list}, convertida a tipo bool es {booVar}. ')