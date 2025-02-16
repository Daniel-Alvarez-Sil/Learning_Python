string1 = 'prueba 1'
string2 = string1.capitalize()

print(f'Mensaje 1: {string1}, ID: {hex(id(string1))}')
print(f'Mensaje 2: {string2}, ID: {hex(id(string2))}')

string1 += ' de adición'
print(f'Mensaje 1: {string1}, ID: {hex(id(string1))}')

